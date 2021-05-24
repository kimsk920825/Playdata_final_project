플레이데이터 최종 프로젝트

황영범, 황정현, 편효범, 김승규

저성능의 라즈베리파이는 고성능이 요구되는 실시간 객체 감지 모델을 실행하기가 어렵다
따라서 라즈베리파이는 실시간 영상을 고성능 디바이스로 스트리밍하고
고성능 디바이스에서 실시간 객체 감지 모델을 실행한다
그리고 감지된 데이터를 다시 라즈베리파이로 전송하여 마스크 착용 상태에 맞게 LED 모듈과
gTTS를 이용한 음성을 통해 출입인원을 안내한다
여기서 마스크 착용 상태를 구분할 실시간 객체 감지 도구로
YOLOv5를 이용하여 마스크 착용, 미착용, 오착용을 구분하도록 했다

공공 안전 감시 시스템 (마스크 감지) 프로젝트 실행순서

1.
라즈베리파이에서 mjpg-streamer 실행
터미널에서
sh mjpg.sh
입력

2.
라즈베리파이에서 final_project.py 실행 

3. 
PC에서 detect.py 실행
터미널에서
python ./yolov5/detect.py --weights withAugmentation_e150.pt --conf 0.4 --source http://[IP주소]:[PORT]/?action=stream
입력

4.
프로젝트 실행

개인 코드 nbviewer: https://nbviewer.jupyter.org/gist/kimsk920825/a1fb3a907518ef97d2ea6aae0e4a9d78/%E1%84%80%E1%85%B5%E1%86%B7%E1%84%89%E1%85%B3%E1%86%BC%E1%84%80%E1%85%B2_Model.ipynb

