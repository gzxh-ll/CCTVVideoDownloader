# 央视频下载器

欢迎使用央视频下载器！该程序允许您从[央视网](https://tv.cctv.com)下载视频 ~~，并支持多线程下载。~~ 暂不支持多线程下载。以下是该程序的一些主要功能和使用说明。

## 功能特点

- 获取节目列表信息并选择要下载的节目
- ~~支持多线程下载以加快下载速度~~
- ~~支持从MP4链接中下载视频内容~~
- 支持从M3U8链接中下载视频内容
- 支持合并下载完成的视频片段为单个视频文件

## 使用方法

1. **配置节目单**

   您可以选择导入[节目单](#cdi)文件来配置要下载的节目信息。导入后，您可以选择特定的节目进行下载。
   **注意：新导入的节目单会覆盖旧的节目列表！**

2. **刷新视频列表**

   选择一个节目后，点击`刷新列表`按钮来获取该节目下的视频列表信息。您可以在列表中选择要下载的具体视频。

3. **下载视频**

   选择完视频后，点击`下载视频`按钮开始下载。下载过程会显示在界面中，包括下载进度和状态。

4. **合并视频文件**

   下载完成后，程序会自动将下载的视频片段合并为单个视频文件，以便更方便地查看。

## 配置设置

~~您可以通过`设置`菜单来配置下载的一些参数，包括保存路径、线程数以及是否进行转码等设置。~~
您可以通过`设置`菜单来配置下载的一些参数,功能有待更新。

## 帮助与反馈

如果您在使用过程中遇到任何问题或有任何建议，请随时联系我们。我们会尽力提供帮助和改进程序。

## 关于

感谢您使用央视频下载器！如有任何疑问或建议，请提交[issues](https://github.com/letr007/CCTVVideoDownload/issues)。

---

## 节目单{#cdi}

节目单文件以`.cdi`结尾，以`JSON`格式存储，程序会以JSON方式加载其内容。

下面是一段示例：
```json
{
    "1":{                           // 序号
        "name":"新闻周刊",           // 要显示的名称
        "id":"TOPC1451559180488841" // 节目的id
    },
    "2":{
        "name":"世界周刊",
        "id":"TOPC1451558687534149"
    },
    "3":{
        "name":"今日说法",
        "id":"TOPC1451464665008914"
    }
}
```
导入后的效果：
[Oh,图片走丢了](https://pic.imgdb.cn/item/65c6cad89f345e8d03201d68.png)

**This cross-platform app was generated by** `Briefcase`
