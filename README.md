# MagicTime
sublime text时间日期和时间戳之间的转换插件

## 默认转换的格式
    
    >可以通过"Package Settings"来配置转换规则
    >以下是默认的转换规则

    1: 1536768000 -> 2018-9-13 12:00:00
    2: 2018-9-13 -> 1536768000
    3: 2018/9/13 -> 1536768000
    4: 2018年9月13 -> 1536768000
    5: 2018年9月13日 -> 1536768000
    6: 2018-9-13 00:00:00 -> 1536768000
    7: 2018/9/13 00:00:00 -> 1536768000
    8: 2018年9月13 00:00:00 -> 1536768000
    9: 2018年9月13日 00:00:00 -> 1536768000


## 安装

    1.使用 'ctrl+shift+p' 调出命令，执行 'Package Control:Install Package' 命令。

    2.搜索 'MagicTime' 回车即可安装。

    >目前官方包还未收录，可以通过以下方式进行安装。

    1.使用 'ctrl+shift+p' 调出命令，执行 'Package Control:Add Repository' 命令。
    
    2.将 'https://github.com/nivin-studio/MagicTime' 此链接添加进去。

    3.使用 'ctrl+shift+p' 调出命令，执行 'Package Control:Install Package' 命令。

    4.搜索 'MagicTime' 回车即可安装。

## 使用
#### 时间戳解码

    1.选择需要转换的时间戳文字，鼠标右键选择 '时间戳解码' 即可转换对应的时间日期。


#### 时间戳编码

    1.选择需要转换的时间日期文字，鼠标右键选择 '时间戳编码' 即可转换对应的时间戳。


#### 生成时间戳

    1.鼠标右键选择 '生成时间戳' 即可在光标所在位置添加当前时间的时间戳。
