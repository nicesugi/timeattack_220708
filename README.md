# timeattack_220708
타임어택 / 7월 8일 / 미니 채용 관리 시스템 : 특정 채용 공고에 지원자가 지원하는 API 구현


**1. 프로젝트에 jwt 인증을 사용해서 access token을 발급하도록 simple jwt 설정**

- ACCESS_TOKEN_LIFETIME은 50분, REFRESH_TOKEN_LIFETIME은 1일로 설정

**2. 지원자가 언제, 어떤 채용공고에 지원했는지 저장할 수 있도록 모델을 추가해보세요.**

**3. 2번에서 만든 모델의 객체를 직렬화 하기 위한 Serializer 구현**
**4. 채용 공고에 지원하는 API 구현 (이력서는 이미 있어서 지원하면 저장되있는 이력서로 자동으로 지원된다고 가정)**

- 지원하는 유저정보는 별도로 받지 않고 발급받은 access token 으로 인증할 것

- request 예시(Bearer Token)

**5. 유저타입이 “candidate”일 때만 인가되도록 BasePermission을 상속받아서 IsCandidateUser 구현 후에 4번 API에 permission class로 지정할 것**
