---
layout: article
titles:
  # @start locale config
  en      : &EN       Research
  ko      : &KO       연구분야
  # @end locale config
key: research
show_title: false
---


## Our Vision

***데이터의 잠재력은 무한하지만, 그것을 담아내는 하드웨어는 유한합니다.***

데이터의 가치를 최대로 이끌어내는 기술은 종종 모델의 복잡성, 막대한 연산량, 그리고 개별 장비의 물리적 한계라는 현실의 벽에 부딪힙니다. 우리 연구실의 비전은 바로 이 간극을 메우고, **하드웨어의 제약이 더 이상 데이터 활용의 장벽이 되지 않는 미래**를 만드는 것입니다.

이를 위해 우리 연구실은 **데이터 마이닝, 기계 학습, 정보 검색** 기술을 기반으로 **두 가지 핵심 전략**을 통해 문제에 접근합니다.

첫째, 우리는 알고리즘 자체를 더 똑똑하고 가볍게 만듭니다. 고차원 데이터의 본질을 꿰뚫는 **'효율적인 기계학습(Efficient Machine Learning)'** 연구를 통해, 제한된 자원만으로도 복잡한 데이터를 빠르고 정확하게 학습하고 탐색하는 기술을 개발합니다.

둘째, 우리는 알고리즘이 동작하는 물리적 환경을 깊이 이해합니다. 거대한 서버 클러스터부터 손안의 작은 엣지 디바이스까지, 어떤 환경에서도 최적의 성능을 발휘하는 **대규모 데이터 마이닝(Large-scale Data Mining)** 기술을 통해 데이터 처리의 물리적 한계를 극복합니다.

궁극적으로, 우리의 연구는 데이터가 존재하는 모든 곳에서 그 가치가 막힘없이 흐를 수 있도록 하는 기술적 토대를 마련하는 것을 목표로 합니다. 우리의 알고리즘이 현실 세계의 복잡한 문제를 해결하고, 새로운 가능성을 여는 핵심 동력이 될 것이라 믿습니다.

<!-- 데이터가 세상의 중심이 된 시대, 그 안에 숨겨진 가치는 무한하지만 **데이터의 규모와 복잡성**은 이를 활용하는 데 큰 장벽이 되고 있습니다.

우리 연구실은 **데이터 마이닝, 기계 학습, 정보 검색** 등의 기술을 활용하여 대규모 데이터를 효율적으로 처리하고 분석할 수 있는 확장 가능한 알고리즘을 연구 및 개발합니다.
특히, 모델 압축, 표현 학습 등을 통해 복잡한 데이터를 효과적으로 학습시키는 **Efficient Machine Learning** 분야와 분산/병렬 시스템이나 엣지 디바이스와 같은 제약된 환경에서 대규모 데이터를 빠르게 처리하는 **Large-scale Data Mining** 분야에 집중합니다.

우리의 목표는 단순히 빠른 알고리즘을 넘어, 하드웨어와 같은 물리적 제약 없이 누구나 데이터의 잠재력을 최대로 이끌어내는 기술적 토대를 마련하는 것입니다.
이를 통해 현실 세계의 복잡한 문제 해결에 기여하고 데이터 기반 혁신을 선도하고자 합니다. -->


## Research Interests

### Efficient Machine Learning

**복잡한 데이터를 어떻게 하면 제한된 자원 내에서 가장 효율적으로 학습하고 표현할 수 있을까요?**

현대의 기계학습 모델, 특히 딥러닝 모델은 놀라운 성능을 보여주지만, 그 이면에는 천문학적인 양의 연산과 막대한 메모리 사용량이라는 장벽이 존재합니다.
본 연구실은 이러한 현실적인 제약을 극복하고, 고성능 인공지능 기술을 누구나 활용할 수 있도록 만드는 '효율적인 기계학습' 연구에 집중합니다.

이를 위해 우리는 세 가지 핵심 분야를 연구합니다.
첫째, 고차원의 원본 데이터가 가진 본질적인 의미는 유지하면서, 다루기 쉬운 저차원의 벡터로 압축하여 표현하는 **표현 학습(Representation Learning)**입니다. 이는 후속 학습 과정의 속도와 정확성을 비약적으로 향상시키는 기반이 됩니다.
둘째, 이미 학습된 모델의 성능 저하를 최소화하면서 크기와 연산량을 줄여, 실제 서비스 환경에 탑재될 수 있도록 만드는 **모델/데이터 압축(Model/Data Compression)** 기술을 연구합니다.
마지막으로, 수십억 개의 데이터 속에서도 원하는 정보를 실시간으로 찾아낼 수 있도록 데이터의 특성을 고려하여 색인(Index)을 구축하는 **데이터 구조화 및 탐색(Data Structuring and Search)** 알고리즘을 개발합니다.

#### Publications
- SkySearch: Satellite Video Search at Scale, KDD, 2025 (최우수 국제 학회)
- Latent Representation Generation for Efficient Content-Based Image Retrieval in Weather Satellite Images Using Self-Supervised Segmentation, BigComp, 2024
- Enhancing Heterophilic Graph Neural Network Performance through Label Propagation in K-Nearest Neighbor Graphs, BigComp, 2024

### Large-scale Data Mining

**단 한 대의 컴퓨터로는 더 이상 감당할 수 없는 대규모 데이터를 어떻게 하면 빠르고 효율적으로 처리할 수 있을까요?**

데이터의 크기가 테라바이트(TB), 페타바이트(PB)를 넘어서면서, 이제는 알고리즘의 이론적 성능뿐만 아니라 그것이 동작하는 하드웨어 환경을 이해하는 것이 무엇보다 중요해졌습니다. 우리 연구실은 알고리즘이 실제 물리적 시스템 위에서 최적의 성능을 낼 수 있도록 하는 '하드웨어 친화적인(Hardware-Aware)' 데이터 마이닝 기술을 설계합니다.

우리의 연구는 크게 두 가지 상반된 컴퓨팅 환경에 초점을 맞춥니다. 하나는 수백, 수천 대의 서버를 엮어 거대한 문제를 해결하는 **분산/병렬 시스템(Distributed/Parallel Systems)**입니다. 여기서는 데이터를 각 서버에 어떻게 분배하고, 통신 비용을 최소화하며, 특정 서버에 작업이 몰리는 병목 현상을 해결하여 전체 처리 시간을 단축하는 알고리즘을 개발합니다.
다른 하나는 스마트폰, IoT 센서와 같이 컴퓨팅 자원이 극히 부족한 **엣지 디바이스(Edge Devices)**입니다. 이 환경에서는 제한된 메모리와 배터리, 계산 능력 내에서 연산 효율성을 극대화하여, 네트워크 연결 없이도 기기 자체에서 실시간 데이터 분석이 가능한 경량 알고리즘을 연구합니다.


#### Publications
- BTS: Load-Balanced Distributed Union-Find for Finding Connected Components with Balanced Tree Structures, ICDE, 2024 (최우수 국제 학회)
- Efficient Proximity Search in Time-evolving High-dimensional Data using Multi-level Block Indexing, EDBT, 2024 (우수 국제 학회)
- Efficient Distributed Approximate k-Nearest Neighbor Graph Construction by Multiway Random Division Forest, KDD, 2023 (최우수 국제 학회)
- UniCon: A Unified Star-Operation to Efficiently Find Connected Components on a Cluster of Commodity Hardware, PLOS ONE, 2022
- PACC: Large Scale Connected Component Computation on Hadoop and Spark, PLOS ONE, 2020
