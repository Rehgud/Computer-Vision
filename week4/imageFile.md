# 이미지 파일 처리
### 이미지 파일 처리 주요 함수
- function: `cv.imread(filename[, flags]) -> retval`
>- 파일에서 이미지를 읽어오는 함수
>- Parameters
>>- filename: 읽어올 파일의 이름
>>- Flags: 색상 유형을 결정하는 flag(cv::ImreadModes)
- function: `cv.imwrite(filename, img[, params]) -> retval`
>- 이미지를 특정 파일에 저장하는 함수
>- Parameters
>>- filename: 저장할 파일의 이름
>>- Img: 저장하고자 하는 이미지
>>- Flags: 압축 방식을 결정하는 flag(cv::ImwriteFlags)
### 이미지 처리 도구
- java 기반 이미지 처리/분석 도구 사용
- openSource
