# 정렬(sort)

## 정렬이란
원소들을 번호순이나 사전 순서와 같이 일정한 순서대로 열거하는 알고리즘


## 정렬 종류
### Bubble
인접한 두 개의 원소를 비교하며 자리를 교환하는 방식
O(n^2)


### Counting
항목들의 순서를 결정하기 위해 집합에 각 몇 항목이 있는지 세는 작업을 하며 선형 시간에 정렬하는 효율적인 알고리즘


### Selection
저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
1. 주어진 리스트 중에서 최솟값을 찾는다.
2. 그 값을 리스트의 맨 앞에 위치한 값과 교환
3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 반복


### Quick
분할 정복 알고리즘의 하나로, 평균적으로 매우 빠른 수행 속도를 자랑하는 정렬 방법
합병 정렬(merge sort)과 달리 퀵 정렬은 리스트를 비균등하게 분할한다.
1. 리스트 안에 있는 한 요소를 선택한다. 이렇게 고른 원소를 피벗(pivot) 이라고 한다.
2. 피벗을 기준으로 피벗보다 작은 요소들은 모두 피벗의 왼쪽으로 옮겨지고 피벗보다 큰 요소들은 모두 피벗의 오른쪽으로 옮겨진다.
4. 피벗을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬한다.
5. 분할된 부분 리스트에 대하여 순환 호출 을 이용하여 정렬을 반복한다.
6. 부분 리스트에서도 다시 피벗을 정하고 피벗을 기준으로 2개의 부분 리스트로 나누는 과정을 반복한다.
7. 부분 리스트들이 더 이상 분할이 불가능할 때까지 반복한다.
8. 리스트의 크기가 0이나 1이 될 때까지 반복한다.


### Insertion
### Merge
