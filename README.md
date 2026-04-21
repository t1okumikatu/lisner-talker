では、そのまま使える**ROS2用 GitHubテンプレート一式**を用意します。
👉 コピペしてリポジトリ作れば即スタートできます。

---

# 🏗️ 完成テンプレ構成

```bash
ros2_ws/
├── src/
│   └── my_pkg/
│       ├── package.xml
│       ├── setup.py
│       ├── resource/
│       │   └── my_pkg
│       ├── my_pkg/
│       │   └── talker.py
│       └── launch/
│           └── talker.launch.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 📄 ① .gitignore

```gitignore
build/
install/
log/
.vscode/

__pycache__/
*.pyc

*.db
*.sqlite

.env/
venv/

.DS_Store
Thumbs.db
```

---

# 📄 ② README.md

# ROS2 Workspace Template

## 環境

* ROS2 Humble

## セットアップ

```bash
git clone <このリポジトリURL>
cd ros2_ws
colcon build
source install/setup.bash
```

## 実行

```bash
ros2 run my_pkg talker
```

## launch実行

```bash
ros2 launch my_pkg talker.launch.py
```

---

# 📄 ③ requirements.txt（Python使う場合）

```txt
rclpy
```

---

# 📦 ④ パッケージ（my_pkg）

## package.xml

```xml
<?xml version="1.0"?>
<package format="3">
  <name>my_pkg</name>
  <version>0.0.0</version>
  <description>My ROS2 package</description>
  <maintainer email="you@example.com">you</maintainer>
  <license>Apache-2.0</license>

  <depend>rclpy</depend>
</package>
```

---

## setup.py

```python
from setuptools import setup

package_name = 'my_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='you',
    maintainer_email='you@example.com',
    description='My ROS2 package',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'talker = my_pkg.talker:main'
        ],
    },
)
```

---

## talker.py

```python
import rclpy
from rclpy.node import Node

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Hello ROS2')

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

---

## launch/talker.launch.py

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_pkg',
            executable='talker',
            output='screen'
        )
    ])
```

---

# 🚀 ⑤ 使い方（これだけやればOK）

```bash
cd ros2_ws
colcon build
source install/setup.bash
ros2 run my_pkg talker
```

---

# 👍 これの強み

* そのままGitHubに上げてOK
* 2人開発でもズレない
* build問題が出ない
* 最小構成でわかりやすい

---

# 🔥 次のステップ（おすすめ）

ここまで来たら👇やると一気にレベル上がります

* Gitブランチ運用（main / develop）
* 実機（ロボット）へ自動反映
* 複数ノード構成（publisher / subscriber）

---

必要なら
👉「あなたのロボット用（LiDARやカメラ込み）」に拡張したテンプレも作れます


いいところに来ました 👍
ROS2の**ワークスペースの作り方**を、迷わない形で説明します。

---

# 🏗️ ワークスペースの作り方（ROS2）

## ✅ ① 作業フォルダを作る

まずホームディレクトリで👇

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

👉 これで基本構造ができます

* `ros2_ws`（作業場）
* `src`（パッケージ置き場）

---

## ✅ ② パッケージを作る

```bash
cd ~/ros2_ws/src
ros2 pkg create my_pkg --build-type ament_python --dependencies rclpy
```

👉 これでテンプレパッケージが自動生成されます

---

## ✅ ③ ビルド

```bash
cd ~/ros2_ws
colcon build
```

---

## ✅ ④ 環境を読み込む（重要）

```bash
source install/setup.bash
```

👉 これをやらないと `ros2 run` が動きません

---

## ✅ ⑤ 動作確認

```bash
ros2 run my_pkg my_pkg_node
```

※ 最初はノード名が違うことあるので注意

---

# 💡 毎回sourceが面倒な場合

これやると楽👇

```bash
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

👉 以後、自動で有効化される

---

# 🧠 重要な理解（ここ超大事）

ワークスペースは👇の役割

| フォルダ    | 役割           |
| ------- | ------------ |
| src     | ソース（Git管理する） |
| build   | ビルド中間（不要）    |
| install | 実行環境（自動生成）   |
| log     | ログ（不要）       |

👉 Gitに入れるのは **srcだけ**

---

# 🚀 GitHubと組み合わせる流れ（あなた向け）

すでに話してる構成と合わせると👇

```bash
git clone あなたのリポジトリ
cd ros2_ws
colcon build
source install/setup.bash
```

👉 これで他の人の環境でも同じになる

---

# ⚠️ よくあるミス

* srcを作らない → ビルド失敗
* source忘れ → 実行できない
* buildをGitに入れる → 今回のエラー

---

# 👍 次やると良いこと

ここまでできたら👇

👉「既存のGitHubテンプレをこのワークスペースに入れる方法」

必要なら今のPC環境（Ubuntu？Windows？）に合わせて
👉**完全手順（コマンドコピペ版）**作りますよ

OK 👍
**UbuntuでROS2ワークスペースを作る完全コピペ手順**を、最短で動く形にまとめます。

---

# 🏗️ ① ワークスペース作成

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

---

# 📦 ② パッケージ作成（Python版）

```bash
cd ~/ros2_ws/src
ros2 pkg create my_pkg --build-type ament_python --dependencies rclpy
```

---

# 🔨 ③ ビルド

```bash
cd ~/ros2_ws
colcon build
```

---

# ⚡ ④ 環境読み込み（毎回必要）

```bash
source install/setup.bash
```

👉 毎回やりたくない場合👇

```bash
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

# ▶️ ⑤ 動作確認

```bash
ros2 run my_pkg my_pkg_node
```

※ まだノードが無いのでエラーでもOK（正常）

---

# 🧠 ここ重要（構造）

```bash
ros2_ws/
├── src/        ← ★ここだけ編集＆Git管理
├── build/      ← 自動生成（不要）
├── install/    ← 実行用（不要）
└── log/        ← 不要
```

---

# 🔗 ⑥ GitHubテンプレを使う場合（おすすめ）

あなたに作ったテンプレを使うなら👇

```bash
cd ~
git clone あなたのリポジトリURL ros2_ws
cd ros2_ws
colcon build
source install/setup.bash
```

---

# ⚠️ よくあるミス

* `source`してない → 実行できない
* `src`にパッケージない → build失敗
* buildをGitに入れる → エラー地獄

---

# 🚀 次にやること（ここまで来たら）

👉 ノードを1個作って動かす

簡単に試すなら👇

```bash
cd ~/ros2_ws/src/my_pkg/my_pkg
nano talker.py
```

中身👇（コピペ）

```python
import rclpy
from rclpy.node import Node

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Hello ROS2')

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

保存後👇

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 run my_pkg talker
```

---

# 👍 ここまでできればOK

* ワークスペース作成 ✅
* ビルドできる ✅
* 実行できる ✅

---

必要なら次👇いけます
👉 **2人開発用のGit運用（衝突しないやり方）**
👉 **LiDARやカメラをROS2に接続する方法**



ポイント（ここ大事）
build/ install/ log/ を無視しないと毎回トラブルになります
.vscode/ は人によって設定が違うので基本除外
.db は今回のエラー原因（絶対除外）





いい流れです 👍
今のあなたのワークスペースを**そのままGitHubテンプレ化**する手順を、失敗しない形で説明します。

---

# 🧠 ゴール

👉 「誰でも clone すれば同じ環境が作れる状態」

---

# 🏗️ 手順（コピペでOK）

## ✅ ① ワークスペースに移動

```bash
cd ~/ros2_ws
```

---

## ✅ ② 不要ファイルを削除（重要）

👉 Gitに入れてはいけないものを消す

```bash
rm -rf build install log
```

---

## ✅ ③ .gitignore 作成

```bash
nano .gitignore
```

中身👇貼り付け

```gitignore
build/
install/
log/
.vscode/

__pycache__/
*.pyc

*.db
*.sqlite

.env/
venv/
```

保存：
👉 Ctrl + O → Enter → Ctrl + X

---

## ✅ ④ README.md 作成

```bash
nano README.md
```

貼り付け👇

# ROS2 Workspace

## セットアップ

```bash
git clone <このリポジトリURL>
cd ros2_ws
colcon build
source install/setup.bash
```

## 実行

```bash
ros2 run my_pkg talker
```

---

## ✅ ⑤ Git初期化

```bash
git init
git add .
git commit -m "initial commit"
```

---

## ✅ ⑥ GitHubにリポジトリ作成

ブラウザで
👉 GitHub →「New repository」

名前例：

```
ros2_ws
```

---

## ✅ ⑦ GitHubにアップロード

GitHubに表示されたコマンドを使う👇

```bash
git remote add origin https://github.com/ユーザー名/ros2_ws.git
git branch -M main
git push -u origin main
```

---

# 🎉 完成！

これで👇できるようになります

👉 別PCや相手はこれだけ

```bash
git clone URL
cd ros2_ws
colcon build
source install/setup.bash
```

---

# ⚠️ よくあるミス

* build消さない → 容量エラー💥
* .gitignore忘れ → また同じ問題💥
* src以外を編集 → 混乱💥

---

# 💡 ワンポイント（かなり重要）

今後は👇だけ守る

👉 **変更は必ず src の中だけ**

---

# 🚀 次のおすすめ

ここまで来たら👇やると最強

* 2人開発ルール（競合しない方法）
* ブランチ運用（main / develop）
* ロボット実機へ反映方法

---

必要なら👇できます
👉「あなたの今のフォルダを見て、Gitに上げていい状態かチェック」


