# Doubu

## Doubu_MingJu_0.3.0

兜布知道古诗文小程序,使用小程序云存储,无需配置回调服务,共有条目1万条。

更新了0.2.1版的页面不滚动问题和页面高度问题

数据来源:gushiwen.py

*********************************************************

## Doubu_MiniApp_0.2.1

兜布知道电力小程序,需要配置Doubu_LeanCloud提供回复服务,因服务器资源限制,回复很慢,项目已停止更新,最后版本0.2.1。

![小程序码](DouBu_MiniApp.jpg) 

## Doubu_LeanCloud

一个简单的使用 ChatterBot和Flask 的 LeanCloud 应用,运行于LeanCloud 的 python3环境,为Doubu_MiniApp提供回复服务。

## BaiduBaike_LeanCloud

提供采集百度百科的 LeanCloud 应用,依托百度百科,从一个条目(节点)开始,爬取关联节点的标题和内容,并存储于LeanCloud中,最后在本地运行后调用yml云函数生成.yml文件。

### db.sqlite3

来源于使用train.py得到,基于如下步骤:

1.生成.yml文件

2.把 *.yml 复制到 /home/XXX/.pyenv/versions/3.6.4/lib/python3.6/site-packages/chatterbot_corpus/data/chinese

3.python train.py
