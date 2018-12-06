# coding: utf-8
import leancloud							#requirements leancloud-sdk>=1.0.9,<=2.0.0
# Standard library imports

import random
import time
from lxml import etree
from datetime import datetime, timedelta

import  os


# local imports

DELAY_BASE = 8
TIME_START = time.time()

from functions import Get_Html_String_Use_Private_Proxy,Unset_Private_Proxy,Get_First_Char_Of_Sting,Get_Html_String_Use_phantomjs,Get_Html_String_Use_Local_Proxy


from classgushimingju import GUSHIMINGJU_CLASS
#from agentpool import Class_Proxy

sFileText ='''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head><meta http-equiv="Cache-Control" content="no-siteapp" /><meta http-equiv="Cache-Control" content="no-transform " /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title>
经典名句_古诗文名句_古诗文网
</title>
<script type="text/javascript">
    if ((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i))) {
        window.location.href = "https://m.gushiwen.org/mingju/Default.aspx?p=1&c=&t=";
    } else {

    }
</script>
<link href="/css/skinSo20180726.css" rel="stylesheet" type="text/css" />
<script>
        var _hmt = _hmt || [];
        (function () {
            var hm = document.createElement("script");
            hm.src = "//hm.baidu.com/hm.js?04660099568f561a75456483228a9516";
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(hm, s);
        })();
    </script>
</head>
<body onclick="closeshowBos()">
<div class="main1">
<div class="cont">
<div class="left">
<a href="https://www.gushiwen.org/">古诗文网</a>
</div>
<div class="right">
<div class="son1">
<a style="margin-left:1px;" href="https://www.gushiwen.org/">推荐</a>
<a href="https://www.gushiwen.org/shiwen/">诗文</a>
<a href="/mingju/" style="background-color:#757863;border-bottom:3px solid #F0EFE2;line-height:43px; height:43px;">名句</a>
<a href="/authors/">作者</a>
<a href="/guwen/">古籍</a>
<a href="/user/collect.aspx" rel="nofollow">收藏</a>
<a style="width:65px;" href="/app/" target="_blank">手机版</a>
</div>
<div class="son2">
<div class="search">
<form action="/search.aspx" onsubmit="return selectSearch()" contentType="text/html; charset=utf-8">
<input onkeydown="noajaxkeyUp()" onfocus="setInterval('showBos()',1000)" id="txtKey" name="value" type="text" value="" maxlength="40" autocomplete="off" style="height:25px; line-height:25px; float:left; padding-left:5px; width:264px; font-size:14px; clear:left; border:0px;" />
<input type="submit" style="float:right; width:20px; height:20px; clear:right; margin-top:4px; margin-right:3px; background-image:url(/img/docSearch.png); background-repeat:no-repeat; background-size:20px 20px; border:0px;cursor:pointer;" value="" />
<input id="b" style="display:none;" type="text" />
</form>
</div>
<div id="box"></div>
</div>
</div>
</div>
</div>
<div class="main3">
<div class="left">
<div class="titletype">
<div class="son1"><h1>不限<span>1 / 200+页</span></h1></div>
<div class="son2" style="border-bottom:0px;padding-bottom:15px;">
<div class="sleft">
<span style="width:48px;">主题：</span>
</div>
<div class="sright" style=" width:580px;">
<span style="width:44px;">不限</span>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85">抒情</a>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e5%9b%9b%e5%ad%a3">四季</a>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e5%b1%b1%e6%b0%b4">山水</a>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e5%a4%a9%e6%b0%94">天气</a>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%89%a9">人物</a>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%94%9f">人生</a>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e7%94%9f%e6%b4%bb">生活</a>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e8%8a%82%e6%97%a5">节日</a>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e5%8a%a8%e7%89%a9">动物</a>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e6%a4%8d%e7%89%a9">植物</a>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e9%a3%9f%e7%89%a9">食物</a>
<a style=" width:44px;" href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d">古籍</a>
</div>
</div>
</div>
<div class="sons" style=" padding-bottom:12px;">
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_2d8bb03f1e19.aspx">山有木兮木有枝，心悦君兮君不知。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_4a96c8287eb5.aspx">佚名《越人歌》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_43f5bfba7229.aspx">人生若只如初见，何事秋风悲画扇。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_85e93138ed65.aspx">纳兰性德《木兰词·拟古决绝词柬友》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_7c9202538459.aspx">十年生死两茫茫，不思量，自难忘。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_567fcf6ffefb.aspx">苏轼《江城子·乙卯正月二十日夜记梦》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_e87e6b55ba7e.aspx">曾经沧海难为水，除却巫山不是云。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_bd4224133394.aspx">元稹《离思五首·其四》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_a1e34e2152e2.aspx">玲珑骰子安红豆，入骨相思知不知。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_a2b349dd32e8.aspx">温庭筠《南歌子词二首 / 新添声杨柳枝词》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_05cbbd4b3d22.aspx">人生如逆旅，我亦是行人。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_330cfc1476ad.aspx">苏轼《临江仙·送钱穆父》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_c3ecb42ab3d7.aspx">只愿君心似我心，定不负相思意。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_d096804a25ff.aspx">李之仪《卜算子·我住长江头》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_55fd5f7d549c.aspx">平生不会相思，才会相思，便害相思。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_c439b578d976.aspx">徐再思《折桂令·春情》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_c77db31d67cb.aspx">入我相思门，知我相思苦。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_169ff9fbafcb.aspx">李白《三五七言 / 秋风词》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_ee4350c22862.aspx">山无陵，江水为竭。冬雷震震，夏雨雪。天地合，乃敢与君绝。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_4ef2774ed20a.aspx">佚名《上邪》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_60716983a3d1.aspx">愿得一心人，白头不相离。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_a416ac373919.aspx">卓文君《白头吟》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_777764b0d152.aspx">两情若是久长时，又岂在朝朝暮暮。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_e83cadaaf394.aspx">秦观《鹊桥仙·纤云弄巧》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_014203a41f16.aspx">去年今日此门中，人面桃花相映红。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_2449fc7a9986.aspx">崔护《题都城南庄》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_6b902526f6f5.aspx">人生自是有情痴，此恨不关风与月。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_475f8e88862c.aspx">欧阳修《玉楼春·尊前拟把归期说》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_f65c48d99ca7.aspx">雨打梨花深闭门，忘了青春，误了青春。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_826758a2d666.aspx">唐寅《一剪梅·雨打梨花深闭门》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_201eedc0bbf1.aspx">花自飘零水自流。一种相思，两处闲愁。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_b7f6fef5bb0b.aspx">李清照《一剪梅·红藕香残玉簟秋》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_48d25baf3cd0.aspx">一日不见兮，思之如狂。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_13f153478a2a.aspx">司马相如《凤求凰 / 琴歌》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_35b8abf2919e.aspx">问世间，情为何物，直教生死相许？</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_8a860f142c0a.aspx">元好问《摸鱼儿·雁丘词 / 迈陂塘》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_5b12ce0a3539.aspx">身无彩凤双飞翼，心有灵犀一点通。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_05c6c4ccf634.aspx">李商隐《无题·昨夜星辰昨夜风》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_ab77932b6edd.aspx">世间无限丹青手，一片伤心画不成。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_1e6e5884e818.aspx">高蟾《金陵晚望》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_257489057416.aspx">少年不识愁滋味，爱上层楼。爱上层楼。为赋新词强说愁。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_2ee36eb2ccf7.aspx">辛弃疾《丑奴儿·书博山道中壁》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_ba800fd1c88a.aspx">滚滚长江东逝水，浪花淘尽英雄。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_284e20a25958.aspx">杨慎《临江仙·滚滚长江东逝水》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_833b978f2ea4.aspx">执子之手，与子偕老。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_73b3c6badf1b.aspx">佚名《击鼓》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_a19f120507df.aspx">一往情深深几许？深山夕照深秋雨。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_5f118f979884.aspx">纳兰性德《蝶恋花·出塞》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_940a59e42252.aspx">林花谢了春红，太匆匆。无奈朝来寒雨，晚来风。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_2dcf6f7cfbbc.aspx">李煜《相见欢·林花谢了春红》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_1eded5a45df0.aspx">自在飞花轻似梦，无边丝雨细如愁。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_8cd9a96daaa4.aspx">秦观《浣溪沙·漠漠轻寒上小楼》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_f069add65f2e.aspx">春宵一刻值千金，花有清香月有阴。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_eafb4ea8a749.aspx">苏轼《春宵·春宵一刻值千金》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_12d07b956d3b.aspx">春风得意马蹄疾，一日看尽长安花。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_6650a905deea.aspx">孟郊《登科后》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_aa74d055f80d.aspx">一生大笑能几回，斗酒相逢须醉倒。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_60e54be43423.aspx">岑参《凉州馆中与诸判官夜集》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_4e55864c0ddf.aspx">此情可待成追忆，只是当时已惘然。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_1921957e6e83.aspx">李商隐《锦瑟》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_0259d499afe3.aspx">思悠悠，恨悠悠，恨到归时方始休。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_10ff29925d73.aspx">白居易《长相思·汴水流》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_558faccdc2aa.aspx">一声梧叶一声秋，一点芭蕉一点愁，三更归梦三更后。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_39ad02580f79.aspx">徐再思《水仙子·夜雨》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_35b498946e7f.aspx">菩提本无树，明镜亦非台。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_d027e5edc80f.aspx">惠能《菩提偈》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_38049d27ea43.aspx">时光只解催人老，不信多情，长恨离亭，泪滴春衫酒易醒。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_8cc45971b842.aspx">晏殊《采桑子·时光只解催人老》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_ce0a479cd5bd.aspx">人面不知何处去，桃花依旧笑春风。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_2449fc7a9986.aspx">崔护《题都城南庄》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_3f444ec1081f.aspx">浮云一别后，流水十年间。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_43e1c0daacca.aspx">韦应物《淮上喜会梁川故人 / 淮上喜会梁州故人》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_ad4c8bec0c99.aspx">疏影横斜水清浅，暗香浮动月黄昏。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_e1339dc3ff03.aspx">林逋《山园小梅·其一》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_b9288e0dd753.aspx">抽刀断水水更流，举杯消愁愁更愁。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_731e2a19594e.aspx">李白《宣州谢脁楼饯别校书叔云 / 陪侍御叔华登楼歌》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_2f0ea34a03a6.aspx">昨夜西风凋碧树，独上高楼，望尽天涯路。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_902b7c60788a.aspx">晏殊《蝶恋花·槛菊愁烟兰泣露》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_4a894848679b.aspx">若是前生未有缘，待重结、来生愿。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_80847c0addf5.aspx">乐婉《卜算子·答施》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_e5fa91382cf4.aspx">取次花丛懒回顾，半缘修道半缘君。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_bd4224133394.aspx">元稹《离思五首·其四》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_0596ce87f7a3.aspx">怕相思，已相思，轮到相思没处辞，眉间露一丝。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_71a85f935e90.aspx">俞彦《长相思·折花枝》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_6c1351d9a6b8.aspx">溪云初起日沉阁，山雨欲来风满楼。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_65bc4719e0b1.aspx">许浑《咸阳城东楼 / 咸阳城西楼晚眺 / 西门》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_378669d9c741.aspx">似此星辰非昨夜，为谁风露立中宵。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_3b1108c2df7b.aspx">黄景仁《绮怀》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_7a64dc96265e.aspx">近水楼台先得月，向阳花木易为春。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_8c0e2aecf46a.aspx">苏麟《断句》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_22d0184eed82.aspx">还君明珠双泪垂，恨不相逢未嫁时。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_7bfee4dfbfe0.aspx">张籍《节妇吟·寄东平李司空师道》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_6b7c41fd17b0.aspx">君埋泉下泥销骨，我寄人间雪满头。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_de2ba4e71def.aspx">白居易《梦微之》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_3534f4ba7340.aspx">夜月一帘幽梦，春风十里柔情。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_225cb1230cb7.aspx">秦观《八六子·倚危亭》</a>
</div>
<div class="cont" style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_5f22f6002499.aspx">问君能有几多愁？恰似一江春水向东流。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_3574610d74e0.aspx">李煜《虞美人·春花秋月何时了》</a>
</div>
<div class="cont" style=" margin-top:12px;">
<a style=" float:left;" target="_blank" href="/mingju/juv_a25e9428db6e.aspx">一骑红尘妃子笑，无人知是荔枝来。</a><span style=" color:#65645F; margin-top:-7px; float:left; margin-left:5px; margin-right:10px;">____</span><a style=" float:left;" target="_blank" href="/shiwenv_ccf0369362c7.aspx">杜牧《过华清宫绝句三首》</a>
</div>
</div>
<form id="FromPage" method="get" action="/mingju/Default.aspx" onsubmit="return PageSubmit()">
<div class="pagesright">
<a class="amore" href="/mingju/default.aspx?p=2&c=&t=">下一页</a>
<a style=" color:#808080;background-color:#e7e6d8;">上一页</a>
<span style=" background-color:#E1E0C7; border:0px; margin-top:22px; width:auto;">/ 200+页</span>
<span class="curent"><input id="putpage" name="p" value="1" autocomplete="off" onblur="SubPage()" /></span>
<label id="temppage" style="display:none;">1</label>
<label id="sumPage" style="display:none;">200</label>
<input type="hidden" name="t" value="" />
<input type="hidden" name="c" value="" />
</div>
</form>
</div>
<div class="right">
<div class="sons">
<div class="title">
<div class="titleleft"></div>
主题
</div>
<div class="cont">
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85">抒情</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%9b%9b%e5%ad%a3">四季</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%b1%b1%e6%b0%b4">山水</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%a4%a9%e6%b0%94">天气</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%89%a9">人物</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%94%9f">人生</a>
<a href="/mingju/Default.aspx?p=1&c=%e7%94%9f%e6%b4%bb">生活</a>
<a href="/mingju/Default.aspx?p=1&c=%e8%8a%82%e6%97%a5">节日</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8a%a8%e7%89%a9">动物</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%a4%8d%e7%89%a9">植物</a>
<a href="/mingju/Default.aspx?p=1&c=%e9%a3%9f%e7%89%a9">食物</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d">古籍</a>
</div>
</div>
<div class="abcd">
<script type="text/javascript" src="//aa.gushiwen.org/source/js/site/juyo.js?qlatnkin=r"></script>
</div>
<div class="sons">
<div class="title">
<div class="titleleft"></div>
分类
</div>
<div class="cont">
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e7%88%b1%e6%83%85">爱情</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e5%8f%8b%e6%83%85">友情</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e7%a6%bb%e5%88%ab">离别</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e6%80%9d%e5%bf%b5">思念</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e6%80%9d%e4%b9%a1">思乡</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e4%bc%a4%e6%84%9f">伤感</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e5%ad%a4%e7%8b%ac">孤独</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e9%97%ba%e6%80%a8">闺怨</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e6%82%bc%e4%ba%a1">悼亡</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e6%80%80%e5%8f%a4">怀古</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e7%88%b1%e5%9b%bd">爱国</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%8a%92%e6%83%85&t=%e6%84%9f%e6%81%a9">感恩</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%9b%9b%e5%ad%a3&t=%e6%98%a5%e5%a4%a9">春天</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%9b%9b%e5%ad%a3&t=%e5%a4%8f%e5%a4%a9">夏天</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%9b%9b%e5%ad%a3&t=%e7%a7%8b%e5%a4%a9">秋天</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%9b%9b%e5%ad%a3&t=%e5%86%ac%e5%a4%a9">冬天</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%b1%b1%e6%b0%b4&t=%e5%ba%90%e5%b1%b1">庐山</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%b1%b1%e6%b0%b4&t=%e6%b3%b0%e5%b1%b1">泰山</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%b1%b1%e6%b0%b4&t=%e6%b1%9f%e6%b2%b3">江河</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%b1%b1%e6%b0%b4&t=%e9%95%bf%e6%b1%9f">长江</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%b1%b1%e6%b0%b4&t=%e9%bb%84%e6%b2%b3">黄河</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%b1%b1%e6%b0%b4&t=%e8%a5%bf%e6%b9%96">西湖</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%b1%b1%e6%b0%b4&t=%e7%80%91%e5%b8%83">瀑布</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%a4%a9%e6%b0%94&t=%e5%86%99%e9%a3%8e">写风</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%a4%a9%e6%b0%94&t=%e5%86%99%e4%ba%91">写云</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%a4%a9%e6%b0%94&t=%e5%86%99%e9%9b%a8">写雨</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%a4%a9%e6%b0%94&t=%e5%86%99%e9%9b%aa">写雪</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%a4%a9%e6%b0%94&t=%e5%bd%a9%e8%99%b9">彩虹</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%a4%a9%e6%b0%94&t=%e5%a4%aa%e9%98%b3">太阳</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%a4%a9%e6%b0%94&t=%e6%9c%88%e4%ba%ae">月亮</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%a4%a9%e6%b0%94&t=%e6%98%9f%e6%98%9f">星星</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%89%a9&t=%e5%a5%b3%e5%ad%90">女子</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%89%a9&t=%e7%88%b6%e4%ba%b2">父亲</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%89%a9&t=%e6%af%8d%e4%ba%b2">母亲</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%89%a9&t=%e8%80%81%e5%b8%88">老师</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%89%a9&t=%e5%84%bf%e7%ab%a5">儿童</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%94%9f&t=%e5%8a%b1%e5%bf%97">励志</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%94%9f&t=%e5%93%b2%e7%90%86">哲理</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%94%9f&t=%e9%9d%92%e6%98%a5">青春</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%94%9f&t=%e6%97%b6%e5%85%89">时光</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%94%9f&t=%e6%a2%a6%e6%83%b3">梦想</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%94%9f&t=%e8%af%bb%e4%b9%a6">读书</a>
<a href="/mingju/Default.aspx?p=1&c=%e4%ba%ba%e7%94%9f&t=%e6%88%98%e4%ba%89">战争</a>
<a href="/mingju/Default.aspx?p=1&c=%e7%94%9f%e6%b4%bb&t=%e4%b9%a1%e6%9d%91">乡村</a>
<a href="/mingju/Default.aspx?p=1&c=%e7%94%9f%e6%b4%bb&t=%e7%94%b0%e5%9b%ad">田园</a>
<a href="/mingju/Default.aspx?p=1&c=%e7%94%9f%e6%b4%bb&t=%e8%be%b9%e5%a1%9e">边塞</a>
<a href="/mingju/Default.aspx?p=1&c=%e7%94%9f%e6%b4%bb&t=%e5%86%99%e6%a1%a5">写桥</a>
<a href="/mingju/Default.aspx?p=1&c=%e8%8a%82%e6%97%a5&t=%e6%98%a5%e8%8a%82">春节</a>
<a href="/mingju/Default.aspx?p=1&c=%e8%8a%82%e6%97%a5&t=%e5%85%83%e5%ae%b5%e8%8a%82">元宵节</a>
<a href="/mingju/Default.aspx?p=1&c=%e8%8a%82%e6%97%a5&t=%e5%af%92%e9%a3%9f%e8%8a%82">寒食节</a>
<a href="/mingju/Default.aspx?p=1&c=%e8%8a%82%e6%97%a5&t=%e6%b8%85%e6%98%8e%e8%8a%82">清明节</a>
<a href="/mingju/Default.aspx?p=1&c=%e8%8a%82%e6%97%a5&t=%e7%ab%af%e5%8d%88%e8%8a%82">端午节</a>
<a href="/mingju/Default.aspx?p=1&c=%e8%8a%82%e6%97%a5&t=%e4%b8%83%e5%a4%95%e8%8a%82">七夕节</a>
<a href="/mingju/Default.aspx?p=1&c=%e8%8a%82%e6%97%a5&t=%e4%b8%ad%e7%a7%8b%e8%8a%82">中秋节</a>
<a href="/mingju/Default.aspx?p=1&c=%e8%8a%82%e6%97%a5&t=%e9%87%8d%e9%98%b3%e8%8a%82">重阳节</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8a%a8%e7%89%a9&t=%e5%86%99%e9%b8%9f">写鸟</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8a%a8%e7%89%a9&t=%e5%86%99%e9%a9%ac">写马</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8a%a8%e7%89%a9&t=%e5%86%99%e7%8c%ab">写猫</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%a4%8d%e7%89%a9&t=%e6%a2%85%e8%8a%b1">梅花</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%a4%8d%e7%89%a9&t=%e6%a2%a8%e8%8a%b1">梨花</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%a4%8d%e7%89%a9&t=%e6%a1%83%e8%8a%b1">桃花</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%a4%8d%e7%89%a9&t=%e8%8d%b7%e8%8a%b1">荷花</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%a4%8d%e7%89%a9&t=%e8%8f%8a%e8%8a%b1">菊花</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%a4%8d%e7%89%a9&t=%e6%9f%b3%e6%a0%91">柳树</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%a4%8d%e7%89%a9&t=%e5%8f%b6%e5%ad%90">叶子</a>
<a href="/mingju/Default.aspx?p=1&c=%e6%a4%8d%e7%89%a9&t=%e7%ab%b9%e5%ad%90">竹子</a>
<a href="/mingju/Default.aspx?p=1&c=%e9%a3%9f%e7%89%a9&t=%e5%86%99%e9%85%92">写酒</a>
<a href="/mingju/Default.aspx?p=1&c=%e9%a3%9f%e7%89%a9&t=%e5%86%99%e8%8c%b6">写茶</a>
<a href="/mingju/Default.aspx?p=1&c=%e9%a3%9f%e7%89%a9&t=%e8%8d%94%e6%9e%9d">荔枝</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e8%ae%ba%e8%af%ad">论语</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e5%8f%b2%e8%ae%b0">史记</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e5%ba%84%e5%ad%90">庄子</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e5%ad%9f%e5%ad%90">孟子</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e4%b8%ad%e5%ba%b8">中庸</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e5%b7%a6%e4%bc%a0">左传</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e5%85%ad%e9%9f%ac">六韬</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e7%b4%a0%e4%b9%a6">素书</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e6%98%93%e4%bc%a0">易传</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e5%a2%a8%e5%ad%90">墨子</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e8%8d%80%e5%ad%90">荀子</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e8%ae%ba%e8%a1%a1">论衡</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e4%b8%89%e7%95%a5">三略</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e8%af%b4%e8%8b%91">说苑</a>
<a href="/mingju/Default.aspx?p=1&c=%e5%8f%a4%e7%b1%8d&t=%e6%96%87%e5%ad%90">文子</a>
</div>
</div>
<div class="abcd">
<script type="text/javascript" src="//aa.gushiwen.org/common/web/ho6k.js?nixqkh=krr"></script>
</div>
</div>
</div>
<div class="main4">
© 2018 <a href="https://www.gushiwen.org/">古诗文网</a> | <a href="https://www.gushiwen.org/shiwen/">诗文</a> | <a href="/mingju/">名句</a> | <a href="/authors/">作者</a> | <a href="/guwen/">古籍</a> | <a href="/jiucuo.aspx?u=" target="_blank" rel="nofollow">纠错</a>
</div>
<script type="text/javascript">
    window.onload = function () {
        setIframeHeight(document.getElementById('external-frame'));
    };
        </script>
<script defer="defer" src="/js/skinso20180608.js" type="text/javascript"></script>
<script defer="defer" src="/js/jquery-3.2.1.min.js" type="text/javascript"></script>
<script defer="defer" src="/js/jquery.qrcode.min.js" type="text/javascript"></script>
</body>
</html>
'''

class Class_Http_Get_GuShiWenMingJu():
	# A class get html and prase it like this url:
	# http://guba.eastmoney.com/news,600683,693158720.html
	# 为解决主页面中夹杂混乱日期的方案
	# 直接返回页面中最后的日期，1、先找zwlitime，返回最后一个，若无，返回zwfbtime
	# <div class="zwfbtime">发表于 2017-08-16 10:45:55 股吧网页版</div>	=楼主，一定有
	# <div class="zwlitime">发表于 2017-12-12  15:53:44</div>			=评论，不一定有

	############## private ################
	def __init__(self):

		self.__BaseUrl = "https://so.gushiwen.org/mingju/"
		self.__dalay = DELAY_BASE					#每个专属代理有一个专属延时，可以根据返回码决定是否增加延时
		#self.__Prase_Page()

	def Get_All(self):


		RefererUrl = 'https://so.gushiwen.org'
		Url = 'https://so.gushiwen.org/mingju/'
		iStartPage = 4

		if(1==iStartPage):
			self.Http_Prase_Page(Url, RefererUrl)
			time.sleep(random.randint(22, 25))
			iStartPage +=1


		print('*************** iStartPage = ',iStartPage)
		for page in range(iStartPage,201):
			RefererUrl = 'https://so.gushiwen.org/mingju/Default.aspx?p=' + str(page-1) + '&t=&c='
			Url = 'https://so.gushiwen.org/mingju/Default.aspx?p=' + str(page) + '&t=&c='
			self.Http_Prase_Page(Url, RefererUrl)
			time.sleep(random.randint(12, 16))

		print('***************** End of Prase *******************')

	def Test(self):

			self.__Print_Page__(sFileText)
			print('***************** End of Prase *******************')


	def Http_Prase_Page(self, Url, RefererUrl):
		aMingJu = []
		iPage = 1
		global TIME_START
		print ( 'TIME:',time.time()-TIME_START )
		TIME_START = time.time()
		while(0==len(aMingJu)):
			id = str(random.randint(0,200))
			print('########### request:',Url)
			Html_Str = Get_Html_String_Use_Private_Proxy(Url, RefererUrl, id)
			#Html_Str = sFileText
			#Html_Str = Get_Html_String_Use_phantomjs(Url)
			#Html_Str = Get_Html_String_Use_Local_Proxy(Url)
			#proxy = Class_Proxy()
			#Html_Str = proxy.Get_Html_String(Url, RefererUrl, False)
			print(id, Get_First_Char_Of_Sting(Html_Str,60))
			aMingJu = self.__Prase_Page(Html_Str)
			print('aMingJu lenth = ',len(aMingJu))
			#iPage = self.__Get_Page_Num(Html_Str)
			time.sleep(random.randint(self.__dalay, self.__dalay + 3))
		for m in aMingJu:
			GUSHIMINGJU_CLASS.Add(m.get('content'),m.get('from'))
			print(m)
		print('******* End of Prase *******',Url)
		time.sleep(random.randint(5, 8))
		return

	def __Prase_Page(self,html_str):
		# 解析一个页面，'阅读\t评论\t标题\t作者\t发表日期\t最后更新'
		aMingJu = []
		selector = etree.HTML(html_str)
		try:
			articleh = selector.xpath('//div[@class="cont"]')
			print("Total:", len(articleh))
			for ainfo in articleh:
				try:
					aTmp = ainfo.xpath('.//a/text()')
					if (len(aTmp) <= 2):
						try:
							#print (str(aTmp[0]), str(aTmp[1]))
							aMingJu.append({'content': str(aTmp[0]), 'from': str(aTmp[1])})
						except:
							print (type(aTmp), aTmp)
				except:
					pass
		except:
			pass
		return aMingJu




	def __Print_Page__(self,html_str):
		#解析一个页面，'阅读\t评论\t标题\t作者\t发表日期\t最后更新'
		print('Print')
		selector = etree.HTML( html_str )
		try:
			articleh = selector.xpath( '//div[@class="cont"]' )
			print( "Total:",len(articleh))
			for ainfo in articleh:
				try:
					sMingYan = ''
					aTmp = ainfo.xpath('.//a/text()')
					if(len(aTmp)<=2):
						try:
							print (str(aTmp[0]),str(aTmp[1]))
						except:
							print (type(aTmp), aTmp)


				except:
					pass
			return len(articleh)
		except:
			return 0

#Test = Class_Http_Get_MingJu()
#Test.Get_All()

