# ChatGPT-3.5-AccessToken-Web
本项目基于使用Access Token的方式实现了网页版 ChatGPT 3.5的前端，不需要openai的api额度，是用<a href="https://github.com/Yidadaa/ChatGPT-Next-Web" target="_blank" title="ChatGPT-Next-Web">
ChatGPT-Next-Web</a>项目进行修改而得，另外本项目需要的后端服务，集成了<a href="https://github.com/pengzhile/pandora" target="_blank" title="pandora项目">pandora项目</a>
# 示例网站
<a href="http://43.136.103.186:3000/" target="_blank" title="示例网站">点击这里查看示例网站</a>


## 主要功能
![Image text](https://github.com/xueandyue/ChatGPT-3.5-AccessToken-Web/blob/main/doc/images/index.jpg)
- 不需要openai的api额度，解决了api体验额度（1分钟只能调用3次api）用完后，频繁买号更改apikey，重启服务的痛点，成本更低
- 自动更新Access Token，解决了pandora需要14天重新获取Access Token、重启服务的痛点
- 完整的 Markdown 支持：LaTex 公式、Mermaid 流程图、代码高亮等等
- 精心设计的 UI，响应式设计，支持深色模式，支持 PWA
- 极快的首屏加载速度（~100kb），支持流式响应
- 隐私安全，所有数据保存在用户浏览器本地
- 预制角色功能（面具），方便地创建、分享和调试你的个性化对话
- 海量的内置 prompt 列表
- 多国语言支持

## 账号，密码

* 只支持chatgpt官方账号，不支持Google,Microsoft,apple第三方登录
* 也可以访问 [这里](https://ai-20230626.fakeopen.com/auth1)验证账号密码。期间访问**不需要梯子**。这意味着你在手机上也可随意使用。



## 部署机器说明
* 在本地或者国内服务器都可以部署，不需要海外服务器


## 部署
* 确保有chatgpt官方账号
* 确保安装了docker，启动了docker
* CODE是设置的访问密码，如果CODE=""则表示不设置密码，如果CODE="123456",则设置密码为123456
* docker pull xueandyue/next-web-pandora:latest
* docker run -e username="你的gpt账号" -e password="你的gpt账号密码" -e CODE="123456" -p 3000:3000 -d xueandyue/next-web-pandora:latest
* 等待5分钟左右，在浏览器访问http://服务器域名(ip):3000/

## 不支持的部署方式
* 不支持k8s部署和Vercel部署


## 本地如何二次开发调试
* 本地安装python3,推荐python3.9 ,至少要python3.7以上版本
* 获取 Access Token
> 部署pandora项目
* 下载pandora项目：git clone https://github.com/pengzhile/pandora.git
* cd pandora
* 新建token.txt文件，把获取到的 Access Token放进去，保存文件
* pip install .
* pandora -s -t token.txt
> 部署本项目
* 安装yarn
* 下载本项目：git clone https://github.com/xueandyue/ChatGPT-3.5-AccessToken-Web.git
* cd ChatGPT-3.5-AccessToken-Web
* 修改.env.local的CODE，如果为空，则表示不需要密码访问
* yarn install && yarn dev
* 在浏览器访问http://localhost:3000/

>PS：如果不是同一机器上部署pandora项目和本项目，又或者部署pandora项目使用非8008端口，那需要修改本项目用到8008端口的url



## 开源协议

> 反对 996，从我开始。
[Anti 996 License](https://github.com/kattgu7/Anti-996-License/blob/master/LICENSE_CN_EN)


## 其他说明


* 项目是站在其他巨人的肩膀上，感谢！
* 喜欢的请给颗星，感谢！
* 不影响PHP是世界上最好的编程语言！
