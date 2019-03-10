<html></html>
<body></body>
<h1></h1>
<p></p>
<a href="http://www.baidu.com"></a>
<img src="baidu.gif" width="104" height="142" />
<br />
<!DOCTYPE HTML>
<!-- This is a comment -->
<hr />
<body style="background-color:red"></body>
<h1 style="font-family:verdana;color:red;font-size:10px;"></h1>
<h1 style="text-align:center"></h1>

<b>定义粗体字体</b>
<big>定义大号字</big>
<em>定义着重文字</em>
<i>定义斜体字</i>
<small>定义小号字</small>
<strong>定义加重语气</strong>
<sub>定义下标字</sub>
<sup>定义上标字</sup>
<ins>定义插入字</ins>
<del>定义删除字</del>

<code>定义计算机代码</code>
<kbd>定义键盘码</kbd>
<samp>定义计算机代码样本</samp>
<tt>定义打字机代码</tt>
<var>定义变量</var>
<pre>定义预格式文本</pre>

<abbr title=“abc”>定义缩写</abbr>
<scronym title=“abc”>定义首字母缩写</acronym>
<address>定义地址</address>
<bdo>定义文字方向</bdo>
<blockquote>定义长的引用</blockquote>
<q>定义短的引用</q>
<cite>定义引用、引证</cite>
<dfn title=“abc”>定义一个定义项目</dfn>

<!-- -->
<!-- [if IE 8]>
	......
<![endif] -->

<head>	<!-- 外部样式表 -->
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>

<head>	<-- 内部样式表 -->
<style type="text/css">
body {background-color:red}
p {margin-left:20px}
</style>
</head>

<p style=:color:red; margin-left:20px>	<!-- 内联样式 -->
This is a paragraph
</p>

<a href="http://www.baidu.com" style="text-decoration:none">
定义一个没有下划线的链接
</a>

<div>定义文档中的节或区域</div>
<span>定义文档中的行内的小块或区域</span>

<a href="http://www.baidu.com">	<!-- 用图像来作链接 -->
<img border="0" src="baidu.gif" />
</a>

<a href="http://www.baidu.com" target="_blank">Visit</a>
<!-- 在新窗口中打开链接 -->

<a name="tips">创建一个书签</a>
<a href="#tips">指向该书签的链接</a>
<a href="http://www.baidu.com/#tips">其他页面中创建指向该锚的链接</a>

<a href="http://www.baidu.com/" target="_top">跳出框架</a>

<a href="mailto:someone@microsoft.com?subject=Hello%20again">
邮件链接 %20替代空格
</a>

<a href="mailto:someone@microsoft.com?
cc=someoneelse@microsoft.com&bcc=andsomeoneelse2@microsoft.com&subject
=Summer%20Party&body=You%20are%20invited%20to%20a%20big%20summer%20party!">
复杂发送邮件！
</a>

<img src="baidu.gif" alt="baidu" /> <!-- 用文字替换图片 -->
<body background="baidu.gif">背景图片</body>
<img src="baidu.gif" align="bottom(middle)(top)" />	<!--设置对齐方式 -->
<img src="baidu.gif" align="left(right)" />	<!-- 图像浮动 -->
<img src="baidu.gif" width="20" height="50" /> <!-- 缩放图片 -->

<!-- 创建图像映射 -->
<img src="planets.jpg"	border="0" usemap="#planetmap" alt="planets" />
<map name="planetmap" id="planetmap">
<area shape="circle" coords="129,161,10" href="mercur.html" target="_blank" alt="Mercury" />
<area shape="rect" coords="0,0,110,260" href="sun.html" target="_blank" alt="Sun" />
<area shape="circle" coords="180,139,14" href="venus.html" target="_blank" alt="Venus" />
</map>

<!-- 普通图像设置为图像映射 -->
<a href="html_ismap.html">
<img src="planets.jpg" ismap />
</a>

<!-- 表格 -->	<!-- 一行两列 -->
<table border="1">
<caption>我的标题</caption>
<tr>
	<th>Heading</th>	<!-- rowspan="2" 跨越两行 colspan="2" 跨越两列 -->
	<th>Another</th>
</tr>
<tr>
	<td>&nbsp;</td>	<!-- 空格占位符 -->
	<td>200</td>
</tr>
</table>

<ul> <li>a</li> <li>b</li> </ul> <!-- 列表 -->
<table cellpadding="10"></table> <!-- 单元格边距 -->
<table cellspacing="10"></table> <!-- 单元格间距 -->
<table bgcolor="red"(background="baidu.gif")></table> <!-- 背景颜色和图片 -->
<th bgcolor="red"(background="baidu.gif")>消费项目....</th>	<!-- 表格单元背景颜色和图片 -->
<th align="left(right)">消费项目....</th>	<!-- 表格单元中排列内容 -->
<table frame="box(above.below.hside.vside)> </table>	<!-- 用frame属性来控制围绕表格的边框 -->

<head>
<style type="text/css">
thead {color:green}
tbody {color:blue;height:50px}
tfoot {color:red}
</style>
</head>
<col align="lift" /> <!-- 定义用于表格列的属性 -->
