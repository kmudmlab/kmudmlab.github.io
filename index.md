---
layout: article
titles:
  # @start locale config
  en      : &EN       Home
  ko      : &KO       홈
  # @end locale config
key: home
show_title: false
---

<div class="mt-4"></div>
<script type="importmap">
  {
    "imports": {
      "sigma": "https://cdnjs.cloudflare.com/ajax/libs/sigma.js/3.0.0/sigma.min.js",
      "graphology": "https://cdn.jsdelivr.net/npm/graphology@0.26.0/dist/graphology.umd.min.js",
      "graphologyLibrary": "https://cdn.jsdelivr.net/npm/graphology-library/dist/graphology-library.min.js"
    }
  } 
</script>

<div id="container" class="home_graph" style="background-color: #fafafa"></div>
<script type="module">
  import * as sigma from "sigma";
  import "graphology";
  import "graphologyLibrary";
  

  const graphData = {% include_relative assets/network_dataset.json %};
  // Create a graphology graph
  const graph = new graphology.Graph();

  const clusterColors = {};
  const getRandomColor = () => {
    return '#' + Math.floor(Math.random() * 16777215).toString(16).padStart(6, '0');
  };
  
  graphData.nodes.forEach(node => {
    const {key, ...attributes} = node;

    // [수정] 클러스터에 따라 색상 지정
    // 이 노드의 클러스터가 아직 색상 맵에 없다면, 새로운 랜덤 색상을 생성하여 할당합니다.
    if (attributes.cluster && !clusterColors[attributes.cluster]) {
      clusterColors[attributes.cluster] = getRandomColor();
    }
    
    // 해당 클러스터의 색상을 노드의 color 속성에 지정합니다.
    attributes.color = clusterColors[attributes.cluster] || '#ccc'; // 클러스터가 없는 경우 회색으로 처리

    attributes.size = attributes.score * 300 + 2;
    attributes.x = Math.random();
    attributes.y = Math.random();
    graph.addNode(key, attributes);
  });

  graphData.edges.forEach(edge => {
    graph.addEdge(edge[0], edge[1], {"color": "#ddd"});
  });

  const settings = graphologyLibrary.layoutForceAtlas2.inferSettings(graph);
  
  // 애니메이션을 위해 주석 처리된 코드를 활성화 합니다.
  function step() {
    graphologyLibrary.layoutForceAtlas2.assign(graph, { settings, iterations: 1 });
    requestAnimationFrame(step);
  }
  requestAnimationFrame(step);

  // Instantiate sigma.js and render the graph
  const s = new Sigma(graph, document.getElementById("container"));

  // --- 이하 드래그 관련 코드는 그대로 유지 ---

  let draggedNode = null;
  let isDragging = false;

  s.on("downNode", (e) => {
    isDragging = true;
    draggedNode = e.node;
    graph.setNodeAttribute(draggedNode, "highlighted", true);
    if (!s.getCustomBBox()) s.setCustomBBox(s.getBBox());
  });

  s.on("moveBody", ({ event }) => {
    if (!isDragging || !draggedNode) return;

    // Get new position of node
    const pos = s.viewportToGraph(event);

    graph.setNodeAttribute(draggedNode, "x", pos.x);
    graph.setNodeAttribute(draggedNode, "y", pos.y);

    // Prevent sigma to move camera:
    event.preventSigmaDefault();
    event.original.preventDefault();
    event.original.stopPropagation();
  });

  const handleUp = () => {
    if (draggedNode) {
      graph.removeNodeAttribute(draggedNode, "highlighted");
    }
    isDragging = false;
    draggedNode = null;
  };
  s.on("upNode", handleUp);
  s.on("upStage", handleUp);

</script>

## Data Mining Lab. @ Kookmin Univ.

Welcome to Data Mining Laboratory in Kookmin University.

## News


## Contact Information

- Phone: +82-2-910-4795
- E-mail: hmpark@kookmin.ac.kr
- Office: Room 403, Future Hall, 77, Jeongneung-ro, Seongbuk-gu, Seoul, Republic of Korea