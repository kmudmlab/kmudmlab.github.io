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

    attributes.size = attributes.score * 200 + 2;
    attributes.x += Math.random()*500;
    attributes.y += Math.random()*500;
    graph.addNode(key, attributes);
  });

  graphData.edges.forEach(edge => {
    graph.addEdge(edge[0], edge[1], {"color": "#ddd"});
  });

  const settings = graphologyLibrary.layoutForceAtlas2.inferSettings(graph);
  
  // 애니메이션 상태를 관리할 변수들
  let layoutAnimationId = null;
  let layoutTimeoutId = null;

  // 레이아웃 애니메이션을 시작하는 함수
  function startLayoutAnimation() {
    // 기존 애니메이션이 있다면 중복 실행 방지
    if (layoutAnimationId) {
      cancelAnimationFrame(layoutAnimationId);
    }
    // 기존 중지 타이머가 있다면 취소
    if (layoutTimeoutId) {
      clearTimeout(layoutTimeoutId);
      layoutTimeoutId = null;
    }
    
    function step() {
      graphologyLibrary.layoutForceAtlas2.assign(graph, { settings, iterations: 1 });
      layoutAnimationId = requestAnimationFrame(step);
    }
    step();
  }

  // 레이아웃 애니메이션을 중지하는 함수
  function stopLayoutAnimation() {
    if (layoutAnimationId) {
      cancelAnimationFrame(layoutAnimationId);
      layoutAnimationId = null;
    }
  }
  
  // 페이지 로드 시 초기 레이아웃 실행
  startLayoutAnimation();
  // 5초 후에 자동으로 중지
  layoutTimeoutId = setTimeout(stopLayoutAnimation, 3000);


  // Sigma 인스턴스 생성
  const s = new Sigma(graph, document.getElementById("container"), {
  });

  s.setSetting("renderHighlightedNodesLabels", true);

  s.setSetting("nodeReducer", (node, data) => {
    const res = { ...data };
    if (node === "data mining") res.highlighted = true;
    return res;
  });

  // --- 드래그 이벤트 핸들러 수정 ---
  let draggedNode = null;
  let isDragging = false;

  s.on("downNode", (e) => {
    isDragging = true;
    draggedNode = e.node;
    graph.setNodeAttribute(draggedNode, "highlighted", true);
    if (!s.getCustomBBox()) s.setCustomBBox(s.getBBox());

    startLayoutAnimation();
  });

  s.on("moveBody", ({ event }) => {
    if (!isDragging || !draggedNode) return;
    const pos = s.viewportToGraph(event);
    graph.setNodeAttribute(draggedNode, "x", pos.x);
    graph.setNodeAttribute(draggedNode, "y", pos.y);
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

    if (layoutTimeoutId) clearTimeout(layoutTimeoutId);
    layoutTimeoutId = setTimeout(stopLayoutAnimation, 2500);
  };
  s.on("upNode", handleUp);
  s.on("upStage", handleUp);

  const dm_node = graph.getNodeAttributes("data mining")


  const camera = s.getCamera();
  camera.animate({ ratio: 0.1, x: 0.43, y: 0.58 }, { duration: 3000 });
</script>

## Data Mining Lab. @ Kookmin Univ.

Welcome to Data Mining Laboratory in Kookmin University.

## News


## Contact Information

- Phone: +82-2-910-4795
- E-mail: hmpark@kookmin.ac.kr
- Office: Room 403, Future Hall, 77, Jeongneung-ro, Seongbuk-gu, Seoul, Republic of Korea