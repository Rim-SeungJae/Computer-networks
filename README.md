<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/>
# Computer-networks
이 저장소는 컴퓨터 네트워크와 관련된 3개의 프로젝트를 담고 있습니다.

# Concurrent-file-copy-program
![net1](https://github.com/dipreez/Computer-networks/assets/50349104/9bd3ff87-c984-4cce-8dc4-96bb462d2562)
프로그램의 실행 과정을 다이어그램으로 나타내었습니다.
1. Program initiate
파이썬 프로그램이 실행되어 시작하는 단계입니다. 로그에 시간을 기록
하기 위하여 이 단계에서 time.time()을 호출하여 프로그램 시작 시간을
변수에 저장해 놓습니다.
2. Repeatedly get input
반복문을 이용하여 계속해서 키보드 입력을 받습니다. Source file name
을 먼저 입력 받고 destination file name을 다음으로 입력 받습니다. 파
일 이름 대신 exit이 입력되면 프로그램을 종료합니다.
3. Terminate
Exit이 입력되어 프로그램을 종료합니다. 프로그램 종료는 sys.exit(0)를
호출하는 것으로 이루어집니다.
4. Create new thread
Source 및 destination 파일명을 모두 입력 받아 복사를 진행하기 위하
여 새로운 쓰레드를 생성하고 실행합니다. 새 쓰레드의 생성은
threading 패키지의 Thread 클래스를 이용합니다.
5. Read&Paste
새로 생성된 자식 쓰레드에서 파일의 복사 작업이 진행됩니다. 한번에
10KB씩 source 파일의 일부를 destination 파일로 복사합니다. 복사가
시작되는 시점과 종료되는 시점에 log.txt 파일에 기록을 남깁니다.

# Web-server-imitation
![net2](https://github.com/dipreez/Computer-networks/assets/50349104/83a61d5d-267a-4d20-8a22-c848c3ca4a8f)
프로그램의 실행 과정을 다이어그램으로 나타내었습니다.
1. Program initiate
파이썬 프로그램이 실행되어 시작하는 단계입니다.
2. Create socket instance
파이썬 socket 패키지의 socket 객체를 생성합니다. 객체 생성시의 인
자로 AF_INET, SOCK_STREAM를 이용합니다.
3. bind(), listen(), accept()
socket 객체의 메서드들을 순서대로 실행하면서 클라이언트와 연결할
준비를 합니다. accept()는 반복문 내에서 반복적으로 실행됩니다. 하나
의 클라이언트와 연결에 성공하면 새로운 쓰레드를 생성하여 해당 쓰
레드에서 클라이언트로부터 데이터를 받을 준비를 합니다.
4. recv()
socket 객체의 recv() 메서드를 실행하여 클라이언트로부터 데이터를 전
송 받습니다. 이번 과제의 경우 HTTP 요청을 받게 됩니다.
5. Try opening requested file
HTTP 요청을 확인하여 클라이언트가 요청한 파일을 여는 시도를 합니
다.
6. Send 404 NOT FOUND
파일을 여는 시도가 FileNotFoundError를 발생시킬 경우 클라이언트에
게 404 NOT FOUND 응답을 보냅니다. Persistent TCP 연결을 지원하기
위해 응답을 보낸 후에는 다시 recv()를 실행하여 새로운 HTTP 요청을
받을 준비를 합니다.
7. Send data with 200 OK
파일을 여는 시도가 성공했을 경우 클라이언트에 200 OK 응답과 해당
파일에 저장된 데이터를 함께 보냅니다. 마찬가지로 응답을 보낸 후에
는 다시 recv()를 실행하여 새로운 HTTP 요청을 받을 준비를 합니다.

# Solving-NAT-traversal-problem
![net3](https://github.com/dipreez/Computer-networks/assets/50349104/e4d22d8e-c75d-4624-a11f-742bf924ecc4)
![net4](https://github.com/dipreez/Computer-networks/assets/50349104/4ad19d4d-c47c-4a6a-a884-1ef3b1825c8f)
각각 server.py와 client.py 의 실행 과정을 다이어그램으로 나타낸 것입니다.
## Server.py
1. Program initiate
파이썬 프로그램이 실행되어 시작하는 단계입니다.
2. Create socket instance
파이썬 socket 패키지의 socket 객체를 생성합니다. UDP 통신을
위해 객체 생성시의 인자로 AF_INET, SOCK_DGRAM을 이용합니
다.
3. bind()
생성한 소켓을 바인딩합니다.
4. recvfrom()
클라이언트들로부터 각종 데이터들을 받습니다.
5. Process received data
클라이언트들로부터 받은 데이터들을 요청의 종류에 따라 처리
합니다. 신규 register 요청이 확인되면 해당 클라이언트의 정보
를 새로 서버에 등록하고 threading의 Timer 객체를 이용해 30
초짜리 타이머를 생성합니다. 그리고 새로 등록된 클라이언트에
게는 현재 서버에 등록된 모든 클라이언트들의 정보를 전송합니
다. 나머지 클라이언트들에게는 새로 등록된 클라이언트의 정보
를 전송합니다. 이미 등록된 클라이언트의 register 요청이 들어
오면 해당 클라이언트의 타이머를 초기화합니다. 클라이언트의
타이머가 초기화가 이루어지지 않고 30초가 지나서 타이머가 끝
나면 새로운 쓰레드를 생성하여 서버에 등록된 해당 클라이언트
의 정보를 삭제합니다. Deregister 요청이 확인되면 해당 클라이
언트의 정보를 서버에서 삭제합니다. 클라이언트의 정보가 서버
에서 삭제됐을 때 모든 클라이언트들에게 삭제된 클라이언트의
정보를 보냅니다.
6. Program exit
파일의 송신이 모두 끝나고, 모든 패킷에 대한 ack를 받은 뒤
프로그램이 종료되는 단계입니다.
## receiver.py
1. Program initiate
파이썬 프로그램이 실행되어 시작하는 단계입니다
2. Create socket instance
파이썬 socket 패키지의 socket 객체를 생성합니다. UDP 통신을
위해 객체 생성시의 인자로 AF_INET, SOCK_DGRAM을 이용합니
다.
3. bind()
생성한 소켓을 바인딩합니다.
4. sendto()
새로운 쓰레드를 생성하여 해당 쓰레드에서 10초마다 서버에
register 요청을 보냅니다.
5. recfrom()
새로운 쓰레드를 생성하여 해당 쓰레드에서 서버나 다른 클라이
언트들로부터 오는 데이터들을 수신합니다. 처음에는 서버에 등
록돼 있는 모든 클라이언트들의 정보를 받아와 기록합니다. 그
다음부터는 서버에 새로 등록되거나 삭제되는 클라이언트의 정
보를 받아서 반영합니다. 혹은 다른 클라이언트로부터 받은 채
팅 메시지를 화면에 출력합니다.
6. Thread terminate
Daemon 값을 True로 설정하여 부모 쓰레드가 종료될 때 자동
으로 receiving thread와 sending thread 모두 종료됩니다.
7. Program exit
파일 수신을 완료하고 프로그램이 종료되는 단계입니다.
