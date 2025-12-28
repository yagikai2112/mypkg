# mypkg
 このリポジトリは2025年度ロボットシステム学にて作成したものです。  
[![test](https://github.com/yagikai2112/mypkg/actions/workflows/test.yml/badge.svg)](https://actions/yagikai2112/mypkg/.github/workflows/test.yml)
## CPU,メモリ使用率チェッカー
mypkg は、ROS 2上で CPU 使用率およびメモリ使用率を取得・配信するノードと，それらを購読してログ出力するリスナーノードを提供するパッケージです。
## テスト環境  
- Ubuntu-22.04  
- ROS 2: Humble  
- Python version: 3.10  
## テストに利用するコンテナについて
本パッケージの GitHub Actions によるテストでは、ryuichiuedaが用意した Docker コンテナ環境をGitHub Actions 上でダウンロードして使用しています。
## 使用方法
以下のコマンドを実行し，ROS 2 のワークスペースの
src ディレクトリ内で mypkg をダウンロードしてビルドしてください。  
```
$ cd ~/ros2_ws/src
$ git clone https://github.com/yagikai2112/mypkg.git
$ cd ~/ros2_ws
$ colcon build
$ source install/setup.bash
```
## 実行方法  
launch ファイルにより，CPU 使用率・メモリ使用率を取得するノードと，
それらを購読するリスナーノードが同時に起動します。  
```
$ ros2 launch mypkg cpu_monitor.launch.py
```
## 出力例
```
[resource_listener-2] [INFO] [1766940375.405980169] [resource_listener]: CPU Usage: 2.6 %
[resource_listener-2] [INFO] [1766940375.406579690] [resource_listener]: Memory Usage: 9.5 %
[resource_listener-2] [INFO] [1766940376.406089801] [resource_listener]: CPU Usage: 0.1 %
[resource_listener-2] [INFO] [1766940376.406655520] [resource_listener]: Memory Usage: 9.5 %
```
## test
CI 用に test.bash を用意しており，以下を確認しています。  
- colcon build が正常に終了すること  
- ros2 launch がエラーなく起動すること  
- CPU・メモリ情報がログに出力されていること  
手動でテストを実行する場合は，以下を実行します。  
```
$ test/test.bash
```
## 補足
表示される CPU 使用率・メモリ使用率は OS 全体の値を基にしてます。  
タスクマネージャー等と数値が異なる場合があるが，取得方法や平均化方法の違いによるものです。  
## 著作権、ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Kaito Yagiuchi
