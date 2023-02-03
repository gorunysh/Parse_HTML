import requests
from requests.auth import HTTPBasicAuth
import xlwt, xlrd
from lxml import html, etree
from xlutils.copy import copy

# <th> = += 1 столбоец
# <tr> = следующия строка
# <td> = следующая ячейка
# rows = строка, cells = столбец

class Adventure_time():

    def txt_for_test(self):
        self.txt_HTML = '''<!DOCTYPE html>
                                
<html xmlns="http://www.w3.org/1999/xhtml" lang="ru" xml:lang="ru" data-xwiki-reference="xwiki:07\. Развитие.Поставщики.WebHome" data-xwiki-document="07\. Развитие.Поставщики.WebHome" data-xwiki-wiki="xwiki" data-xwiki-space="07\. Развитие.Поставщики" data-xwiki-page="WebHome" data-xwiki-isnew="false" data-xwiki-version="150.1" data-xwiki-rest-url="/rest/wikis/xwiki/spaces/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/spaces/%D0%9F%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B8/pages/WebHome" data-xwiki-locale="" data-xwiki-form-token="KO1DhUKZkretSQ5NRixIbg" data-xwiki-user-reference="xwiki:XWiki.pdemidov">
  <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                                                    <title>Поставщики и ЦП - XWiki</title>
                                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                <link rel="shortcut icon" href="/resources/icons/xwiki/favicon.ico?cache-version=1648653678000" />
        <link rel="icon" href="/resources/icons/xwiki/favicon16.png?cache-version=1648653678000" type="image/png" />
        <link rel="icon" href="/resources/icons/xwiki/favicon.svg?cache-version=1648653678000" type="image/svg+xml" />
        <link rel="apple-touch-icon" href="/resources/icons/xwiki/favicon144.png?cache-version=1648653678000" />
                      <link rel="alternate" type="application/x-wiki" title="Edit" href="/bin/edit/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%9F%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B8/WebHome" />
                    <link rel="canonical" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%9F%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B8/" />
                    <meta name="revisit-after" content="7 days" />
<meta name="description" content="Поставщики и ЦП" />
<meta name="keywords" content="wiki" />
<meta name="rating" content="General" />
<meta name="author" content="Александра Субочева" />
<link rel="alternate" type="application/rss+xml" title="Wiki Feed RSS" href="/bin/view/Main/WebRss?xpage=rdf" />
<link rel="alternate" type="application/rss+xml" title="Blog RSS Feed" href="/bin/view/Blog/GlobalBlogRss?xpage=plain" />
                <link href="/webjars/wiki%3Axwiki/bootstrap-switch/3.3.2/css/bootstrap3/bootstrap-switch.min.css" type='text/css' rel='stylesheet'/><link href="/webjars/wiki%3Axwiki/xwiki-platform-tree-webjar/13.10.4/tree.min.css?evaluate=true" type='text/css' rel='stylesheet'/><link href="/webjars/wiki%3Axwiki/selectize.js/0.12.5/css/selectize.bootstrap3.css" type='text/css' rel='stylesheet'/>
    <link href="/webjars/wiki%3Axwiki/drawer/2.4.0/css/drawer.min.css" rel="stylesheet" type="text/css" />
                
                                                                                                                    



<link href="      /bin/skin/skins/flamingo/style.min.css?cache-version=1648654342000&skin=XWiki.DefaultSkin&#38;colorTheme=xwiki%3AFlamingoThemes.Iceberg&#38;colorThemeVersion=1.2
  " rel="stylesheet" type="text/css" media="all" />
<link href="      /bin/skin/skins/flamingo/print.min.css?cache-version=1648654342000&skin=XWiki.DefaultSkin&#38;colorTheme=xwiki%3AFlamingoThemes.Iceberg&#38;colorThemeVersion=1.2
  " rel="stylesheet" type="text/css" media="print" />
        <!--[if IE]>
  <link href="      /bin/skin/skins/flamingo/ie-all.min.css?cache-version=1648654342000&skin=XWiki.DefaultSkin&#38;colorTheme=xwiki%3AFlamingoThemes.Iceberg&#38;colorThemeVersion=1.2
  " rel="stylesheet" type="text/css" />
<![endif]-->
    
    <link rel='stylesheet' type='text/css' href='/bin/skin/resources/css/xwiki.bundle.min.css?cache-version=1648654498000&colorTheme=FlamingoThemes.Iceberg&amp;language=ru'/><link rel='stylesheet' type='text/css' href='/bin/skin/resources/uicomponents/search/searchSuggest.min.css?cache-version=1648654498000'/><link rel='stylesheet' type='text/css' href='/bin/skin/resources/uicomponents/suggest/xwiki.selectize.min.css?cache-version=1648654498000'/><link rel='stylesheet' type='text/css' href='/bin/skin/resources/uicomponents/viewers/tags.min.css?cache-version=1648654498000&colorTheme=FlamingoThemes.Iceberg'/><link rel='stylesheet' type='text/css' href='/bin/skin/resources/uicomponents/viewers/comments.min.css?cache-version=1648654498000'/><link rel='stylesheet' type='text/css' href='/bin/skin/resources/uicomponents/widgets/upload.min.css?cache-version=1648654498000'/><link rel='stylesheet' type='text/css' href='/bin/skin/resources/js/xwiki/viewers/attachments.min.css?cache-version=1648654496000'/><link rel='stylesheet' type='text/css' href='/bin/skin/resources/uicomponents/pagination/pagination.min.css?cache-version=1648654498000'/><link rel='stylesheet' type='text/css' href='/bin/skin/resources/js/xwiki/viewers/information.min.css?cache-version=1648654496000'/>
    <link rel="stylesheet" type="text/css" href="/bin/ssx/Tour/HomepageTour/WebHome?language=ru&amp;docVersion=1.1" /><link rel="stylesheet" type="text/css" href="/bin/ssx/AnnotationCode/Style?language=ru&amp;docVersion=1.1" /><link rel="stylesheet" type="text/css" href="/bin/ssx/AnnotationCode/Settings?language=ru&amp;docVersion=1.1" /><link rel="stylesheet" type="text/css" href="/bin/ssx/Refactoring/Code/RefactoringConfiguration?language=ru&amp;docVersion=1.1" /><link rel="stylesheet" type="text/css" href="/bin/ssx/XWiki/Mentions/MentionsMacro?language=ru&amp;docVersion=1.1" /><link rel="stylesheet" type="text/css" href="/bin/ssx/IconThemes/FontAwesome?language=ru&amp;docVersion=1.1" /><link rel="stylesheet" type="text/css" href="/bin/ssx/XWiki/Notifications/Code/Macro/NotificationsMacro?language=ru&amp;docVersion=1.1" /><link rel="stylesheet" type="text/css" href="/bin/ssx/XWiki/Notifications/Code/NotificationsDisplayerUIX?language=ru&amp;docVersion=1.1" /><link rel="stylesheet" type="text/css" href="/bin/ssx/XWiki/SharePage?language=ru&amp;docVersion=1.1" /><link rel="stylesheet" type="text/css" href="/bin/ssx/XWiki/Like/LikeUIX?language=ru&amp;docVersion=1.1" /><link rel="stylesheet" type="text/css" href="/bin/ssx/Menu/MenuMacro?language=ru&amp;docVersion=1.1&amp;colorTheme=xwiki%3AFlamingoThemes.Iceberg" /><link rel="stylesheet" type="text/css" href="/bin/ssx/Panels/Applications?language=ru&amp;docVersion=1.1" />

    <script src="/webjars/wiki%3Axwiki/requirejs/2.3.6/require.min.js?r=1" data-wysiwyg="true"></script>
<script src="/resources/js/prototype/prototype.min.js?cache-version=1648654494000"></script>
<script data-wysiwyg="true">
// <![CDATA[
                                                require.config({"paths":{"jquery":"/webjars/wiki%3Axwiki/jquery/2.2.4/jquery.min.js?r=1","bootstrap":"/webjars/wiki%3Axwiki/bootstrap/3.4.1/js/bootstrap.min.js?r=1","xwiki-meta":"/resources/js/xwiki/meta.min.js?cache-version=1648654462000","xwiki-entityReference":"/resources/uicomponents/model/entityReference.min.js?cache-version=1648654480000","xwiki-events-bridge":"/resources/js/xwiki/eventsBridge.min.js?cache-version=1648654460000","xwiki-locale-picker":"/bin/skin/skins/flamingo/localePicker.min.js?cache-version=1648654342000","xwiki-l10n":"/webjars/wiki%3Axwiki/xwiki-platform-localization-webjar/13.10.4/l10n.min.js?r=1","iscroll":"/webjars/wiki%3Axwiki/iscroll/5.1.3/build/iscroll-lite.js?r=1","drawer":"/webjars/wiki%3Axwiki/drawer/2.4.0/js/jquery.drawer.min.js?r=1","deferred":"/resources/uicomponents/require/deferred.min.js?cache-version=1648654480000","xwiki-ckeditor-inline":"/bin/jsx/CKEditor/InlineEditor?v=1.61&xwiki-version=13.10.4","xwiki-ckeditor":"/bin/jsx/CKEditor/EditSheet?v=1.61&xwiki-version=13.10.4&fast-diff-version=&bs3typeahead-version=4.0.2"},"shim":{"bootstrap":["jquery"],"drawer":["jquery","iscroll"],"xwiki-entityReference":{"exports":"XWiki"}},"bundles":{},"config":{},"map":{"*":{"jquery":"jQueryNoConflict"},"jQueryNoConflict":{"jquery":"jquery"}}});
define('jQueryNoConflict', ['jquery'], function ($) {
  return $.noConflict();
});
if (window.Prototype && Prototype.BrowserFeatures.ElementExtensions) {
  require(['jquery', 'bootstrap'], function ($) {
    // Fix incompatibilities between BootStrap and Prototype
    var disablePrototypeJS = function (method, pluginsToDisable) {
      var handler = function (event) {
        event.target[method] = undefined;
        setTimeout(function () {
            delete event.target[method];
        }, 0);
      };
      pluginsToDisable.each(function (plugin) { 
          $(window).on(method + '.bs.' + plugin, handler); 
      });
    },
    pluginsToDisable = ['collapse', 'dropdown', 'modal', 'tooltip', 'tab', 'popover'];
    disablePrototypeJS('show', pluginsToDisable);
    disablePrototypeJS('hide', pluginsToDisable);
  });
}
require(['jquery', 'drawer'], function($) {
  $(document).ready(function() {
    $('.drawer-main').closest('body').drawer();
  });
});
window.XWiki = window.XWiki || {};
XWiki.webapppath = "/";
XWiki.servletpath = "bin/";
XWiki.contextPath = "";
XWiki.mainWiki = "xwiki";
// Deprecated: replaced by meta data in the HTML element
XWiki.currentWiki = "xwiki";
XWiki.currentSpace = "07\\. \u0420\u0430\u0437\u0432\u0438\u0442\u0438\u0435.\u041F\u043E\u0441\u0442\u0430\u0432\u0449\u0438\u043A\u0438";
XWiki.currentPage = "WebHome";
XWiki.editor = "";
XWiki.viewer = "";
XWiki.contextaction = "view";
XWiki.skin = 'XWiki.DefaultSkin';
XWiki.docisnew = false;
XWiki.docsyntax = "xwiki/2.1";
XWiki.docvariant = "";
XWiki.blacklistedSpaces = [ "Import","Panels","Scheduler","Stats","XAppClasses","XAppSheets","XAppTemplates","XWiki","WatchCode","WatchSheets","XApp","WatchAdmin","Watch","ColorThemes","AnnotationCode" ];
XWiki.hasEdit = false;
XWiki.hasProgramming = false;
XWiki.hasBackupPackImportRights = false;
XWiki.hasRenderer = true;
window.docviewurl = "/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%9F%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B8/";
window.docediturl = "/bin/edit/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%9F%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B8/WebHome";
window.docsaveurl = "/bin/save/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%9F%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B8/WebHome";
window.docgeturl = "/bin/get/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%9F%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B8/WebHome";
// ]]>
</script>
                                                                                                                                            
    <script src='/resources/uicomponents/model/entityReference.min.js?cache-version=1648654480000'></script>
<script src='/bin/skin/resources/js/xwiki/xwiki.bundle.min.js?cache-version=1648654496000&defer=false&amp;language=ru'></script>
<script src='/bin/skin/skins/flamingo/flamingo.min.js?cache-version=1648654340000&language=ru' defer='defer'></script>
<script src='/bin/skin/resources/uicomponents/search/searchSuggest.min.js?cache-version=1648654482000&h=1255116547' defer='defer'></script>
<script src='/bin/skin/resources/uicomponents/async/async.min.js?cache-version=1648654472000' defer='defer'></script>
<script src='/bin/skin/resources/uicomponents/hierarchy/hierarchy.min.js?cache-version=1648654476000' defer='defer'></script>
<script src='/bin/skin/resources/uicomponents/widgets/tree.min.js?cache-version=1648654348000' defer='defer'></script>
<script src='/bin/skin/resources/uicomponents/suggest/suggestUsersAndGroups.min.js?cache-version=1648654484000&language=ru' defer='defer'></script>
<script src='/bin/skin/resources/uicomponents/exporter/exporter.min.js?cache-version=1648654474000' defer='defer'></script>
<script src='/bin/skin/resources/uicomponents/viewers/tags.min.js?cache-version=1648654488000' defer='defer'></script>
<script src='/bin/skin/resources/uicomponents/viewers/comments.min.js?cache-version=1648654486000&language=ru' defer='defer'></script>
<script src='/bin/skin/resources/uicomponents/widgets/upload.min.js?cache-version=1648654492000&language=ru' defer='defer'></script>
<script src='/bin/skin/resources/js/xwiki/viewers/attachments.min.js?cache-version=1648654468000&language=ru' defer='defer'></script>
<script src='/bin/skin/resources/uicomponents/viewers/history.min.js?cache-version=1648654486000' defer='defer'></script>
<script src='/bin/skin/resources/js/xwiki/viewers/information.min.js?cache-version=1648654468000&language=ru' defer='defer'></script>
<script src='/bin/skin/resources/uicomponents/edit/editableProperty.min.js?cache-version=1648654474000&language=ru' defer='defer'></script>
<script src='/resources/js/scriptaculous/effects.min.js?cache-version=1648654456000' defer='defer'></script>

    <script src='/bin/jsx/AnnotationCode/Settings?language=ru&amp;docVersion=1.1' defer='defer'></script>
<script src='/bin/jsx/TourCode/TourJS?language=ru&amp;docVersion=1.1' defer='defer'></script>
<script src='/bin/jsx/XWiki/Mentions/MentionsMacro?language=ru&amp;docVersion=1.1' defer='defer'></script>
<script src='/bin/jsx/AnnotationCode/Script?language=ru&amp;docVersion=1.1' defer='defer'></script>
<script src='/bin/jsx/IconThemes/FontAwesome?language=ru&amp;docVersion=1.1' defer='defer'></script>
<script src='/bin/jsx/XWiki/Notifications/Code/Macro/NotificationsMacro?language=ru&amp;docVersion=1.1' defer='defer'></script>
<script src='/bin/jsx/XWiki/Notifications/Code/NotificationsDisplayerUIX?language=ru&amp;docVersion=1.1' defer='defer'></script>
<script src='/bin/jsx/XWiki/QuickSearchUIX?language=ru&amp;docVersion=1.1' defer='defer'></script>
<script src='/bin/jsx/XWiki/SharePage?language=ru&amp;docVersion=1.1' defer='defer'></script>
<script src='/bin/jsx/XWiki/Like/LikeUIX?language=ru&amp;docVersion=1.1' defer='defer'></script>
<script src='/bin/jsx/Menu/MenuMacro?language=ru&amp;docVersion=1.1' defer='defer'></script>
<script src='/bin/jsx/Panels/Applications?language=ru&amp;docVersion=1.1' defer='defer'></script>


<script src="/resources/js/xwiki/compatibility.min.js?cache-version=1648654458000" defer="defer"></script>
<script src="/resources/js/xwiki/markerScript.min.js?cache-version=1648654462000" defer="defer"></script>

  </head>
  <body id="body" class="skin-flamingo wiki-xwiki space-07\._Развитие.ЕЖЕДНЕВНЫЙ_СТАТУС_по_поставщикам viewbody hideright  panel-left-width-Medium panel-right-width-Medium drawer drawer-right drawer-close">
<div id="xwikimaincontainer">
<div id="xwikimaincontainerinner">

  <div id="menuview">
      


















  
      <nav class="navbar navbar-default actionmenu">
    <div class="container-fluid">
            <div class="navbar-header">
                  <div id="companylogo">
  <a href="/bin/view/Main/" title="Home" rel="home" class="navbar-brand">
    <img src="/bin/download/FlamingoThemes/Iceberg/logo.svg?rev=1.1" alt="Wiki Logo">
  </a>
</div>

              </div>
            <div id="xwikimainmenu">
    
          <ul class="nav navbar-nav navbar-left">
      <li class="divider" role="separator"></li>
              </ul>
    
          <ul class="nav navbar-nav navbar-right">
        <li>
    <a class="icon-navbar drawer-toggle" id="tmDrawerActivator" title="Меню"><span class="sr-only">Переключить навигацию</span><span class="fa fa-bars"></span></a>
  </li>
                  <li class="navbar-avatar">
<a href="/bin/view/XWiki/pdemidov" class="icon-navbar">
<span class="sr-only">Профиль пользователя</span>
                                <img class="avatar avatar_50" src="/bin/skin/resources/icons/xwiki/noavatar.png?cache-version=1648653678000" alt="Павел Демидов" title="Павел Демидов"></a>
</li>
                   
<li class="dropdown" id="tmNotifications">
<a class="icon-navbar dropdown-toggle" data-toggle="dropdown" role="button" title="Уведомления">
<span class="sr-only">
Переключить навигацию
</span>
<span class="fa fa-bell"></span>
</a>
<ul class="dropdown-menu">
 <li class="notification-uix loading"></li>

</ul>
</li>
                 <li>
<form class="navbar-form globalsearch globalsearch-close form-inline" id="globalsearch" action="/bin/view/Main/Search" role="search">
<label class="hidden" for="headerglobalsearchinput">Поиск</label>
<input type="text" name="text" placeholder="поиск..." id="headerglobalsearchinput" autocomplete="off">
<button type="submit" class="btn" title="Поиск"><span class="fa fa-search"></span></button>
</form>
</li>
            </ul>
    
          </div>    </div>   </nav>
  
  





<div class="drawer-main drawer-default" id="tmDrawer">
  <nav class="drawer-nav" style="transition-timing-function: cubic-bezier(0.1, 0.57, 0.1, 1); transition-duration: 0ms; transform: translate(0px, 0px) translateZ(0px);">
  
                <div class="drawer-brand clearfix">
      <a href="/bin/view/XWiki/pdemidov">
                                      <img class="avatar avatar_120" src="/bin/skin/resources/icons/xwiki/noavatar.png?cache-version=1648653678000" alt="Павел Демидов" title="Павел Демидов">      </a>
      <div class="brand-links">
                  <a href="/bin/view/XWiki/pdemidov" class="brand-user" id="tmUser">Павел Демидов</a>
          <a href="/bin/logout/XWiki/XWikiLogout?xredirect=%2Fbin%2Fview%2F07.%2520%25D0%25A0%25D0%25B0%25D0%25B7%25D0%25B2%25D0%25B8%25D1%2582%25D0%25B8%25D0%25B5%2F%25D0%2595%25D0%2596%25D0%2595%25D0%2594%25D0%259D%25D0%2595%25D0%2592%25D0%259D%25D0%25AB%25D0%2599%2520%25D0%25A1%25D0%25A2%25D0%2590%25D0%25A2%25D0%25A3%25D0%25A1%2520%25D0%25BF%25D0%25BE%2520%25D0%25BF%25D0%25BE%25D1%2581%25D1%2582%25D0%25B0%25D0%25B2%25D1%2589%25D0%25B8%25D0%25BA%25D0%25B0%25D0%25BC%2F" id="tmLogout" rel="nofollow"><span class="fa fa-sign-out"></span> Выход</a>
                                                          </div>
    </div>

                <ul class="drawer-menu">
                                      <li class="drawer-menu-item drawer-category-header"><hr class="hidden">Home</li>
                                                                                        
                                





  <li class="drawer-menu-item">
    <a href="/bin/view/Main/AllDocs" id="tmWikiDocumentIndex">
      <div class="drawer-menu-item-icon">
        <span class="fa fa-book"></span>
      </div>
      <div class="drawer-menu-item-text">Перечень страниц</div>
    </a>
  </li>
                                      





  <li class="drawer-menu-item">
    <a href="/bin/view/Main/UserDirectory" id="tmMainUserIndex">
      <div class="drawer-menu-item-icon">
        <span class="fa fa-user"></span>
      </div>
      <div class="drawer-menu-item-text">Каталог пользователей</div>
    </a>
  </li>
                                





  <li class="drawer-menu-item">
    <a href="/bin/view/Applications/" id="tmMainApplicationIndex">
      <div class="drawer-menu-item-icon">
        <span class="fa fa-th"></span>
      </div>
      <div class="drawer-menu-item-text">Список приложений</div>
    </a>
  </li>
                                                    <li class="drawer-menu-item drawer-category-header"><hr class="hidden">Глобальные</li>
                                        
                                                        





  <li class="drawer-menu-item">
    <a href="/bin/view/WikiManager/">
      <div class="drawer-menu-item-icon">
        <span class="fa fa-list-alt"></span>
      </div>
      <div class="drawer-menu-item-text">Перечень Вики</div>
    </a>
  </li>
                                                                
          </ul>
  </nav>
</div>





  </div>
 <div id="headerglobal">
  <div id="globallinks">
  </div>   <div class="clearfloats"></div>
      
      
      
  </div> 


<div class="contenthideright" id="contentcontainer">
<div id="contentcontainerinner">
<div class="leftsidecolumns">
  <div id="contentcolumn"> 

        
  <div class="main">
  <div id="mainContentArea">
  
   






















                                                                                                                                                                                                                                                                                                                                                                <ol id="hierarchy" class="breadcrumb breadcrumb-expandable" data-entity="07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome" data-id="hierarchy" data-limit="5" data-treenavigation="true" data-entities="{Space xwiki:07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам=07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome}"><li class="wiki dropdown"><a href="/bin/view/Main/"><span class="fa fa-home"></span></a><span class="dropdown-toggle" data-toggle="dropdown"><span class="fa fa-caret-down"></span></span><div class="dropdown-menu">                                                                                                                                                                                    <div class="breadcrumb-tree" data-responsive="true" data-url="/bin/get/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome?outputSyntax=plain&amp;sheet=XWiki.DocumentTree&amp;showTranslations=false&amp;limit=10" data-root="{}" data-draganddrop="false" data-contextmenu="false" data-icons="true" data-edges="true" data-checkboxes="false" data-opento="document:xwiki:07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome" data-finder="false"></div>
</div></li><li class="space dropdown"><a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/">07. Развитие платформенных сервисов</a><span class="dropdown-toggle" data-toggle="dropdown"><span class="fa fa-caret-down"></span></span><div class="dropdown-menu">                                                                                                                                                                                                  <div class="breadcrumb-tree" data-responsive="true" data-url="/bin/get/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome?outputSyntax=plain&amp;sheet=XWiki.DocumentTree&amp;showTranslations=false&amp;limit=10&amp;root=wiki%3Axwiki" data-root="{&quot;type&quot;:&quot;wiki&quot;,&quot;id&quot;:&quot;xwiki&quot;}" data-draganddrop="false" data-contextmenu="false" data-icons="true" data-edges="true" data-checkboxes="false" data-opento="document:xwiki:07\. Развитие.WebHome" data-finder="false"></div>
</div></li><li class="active space dropdown"><a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/">ЕЖЕНЕДЕЛЬНЫЙ СТАТУС по поставщикам</a><span class="dropdown-toggle" data-toggle="dropdown"><span class="fa fa-caret-down"></span></span><div class="dropdown-menu">                                                                                                                                                                                                  <div class="breadcrumb-tree" data-responsive="true" data-url="/bin/get/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome?outputSyntax=plain&amp;sheet=XWiki.DocumentTree&amp;showTranslations=false&amp;limit=10&amp;root=document%3Axwiki%3A07%5C.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5.WebHome" data-root="{&quot;type&quot;:&quot;document&quot;,&quot;id&quot;:&quot;xwiki:07\\. Развитие.WebHome&quot;}" data-draganddrop="false" data-contextmenu="false" data-icons="true" data-edges="true" data-checkboxes="false" data-opento="document:xwiki:07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome" data-finder="false"></div>
</div>      </li></ol>
    
      


    







<div class="xcontent">
  <div class="row document-header">
  <div class="document-info col-xs-12 col-md-7">
                    <div id="document-title"><h1>ЕЖЕНЕДЕЛЬНЫЙ СТАТУС по поставщикам</h1></div>
          <div class="xdocLastModification">
                  Редактировал(а) <span class="wikilink"><a href="/bin/view/XWiki/asubocheva">Александра Субочева</a></span> 2023/02/02 11:04
              </div>
      </div>
      <div class="document-menu col-xs-12 col-md-5">
      


    
                                                  <div id="contentmenu" class="pull-right actionmenu">
                                                            
                        
                                                                    <div class="btn-group" id="tmCreate">
    <a class="btn btn-default" title="Создать" href="/bin/create/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome" role="button" rel="nofollow">
      <span class="fa fa-plus"></span>
              <span class="btn-label">Создать</span>
          </a>
      </div>
      
                                                      <div class="btn-group" id="tmMoreActions">
    <a class="btn btn-default dropdown-toggle" title="Другие действия" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" role="button">
      <span class="fa fa-ellipsis-v"></span>
          </a>
                <ul class="dropdown-menu dropdown-menu-right">
                                <li class="dropdown-header">Управление</li>
                                                                             
                            <li class="">
    <a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/?xpage=copy" id="tmActionCopy" title="Копировать" rel="nofollow"><span class="fa fa-copy"></span> Копировать</a>
  </li>
    
            
                                                    <li class="divider" role="separator"></li>
                  <li class="dropdown-header">Действия</li>
                                                                                      
      
                                                                <li class="">
    <a href="" id="tmExport" title="Экспорт" data-toggle="modal" data-target="#exportModal"><span class="fa fa-download"></span> Экспорт</a>
  </li>
      
                         
    <li class="tme">
    <a href="#Comments" id="tmAnnotationsTrigger" title="Аннотировать" rel="nofollow"><span class="fa fa-edit"></span> Аннотировать</a>
  </li>
                                <li class="">
    <a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/?xpage=print" id="tmPrintPreview" title="Предварительный просмотр" rel="nofollow"><span class="fa fa-print"></span> Предварительный просмотр</a>
  </li>
    
                                  <li class="">
    <a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/?viewer=share" id="tmActionShare" title="Поделиться по email" rel="nofollow"><span class="fa fa-envelope-o"></span> Поделиться по email</a>
  </li>
          
        
            
                                                                  <li class="divider" role="separator"></li>
                  <li class="dropdown-header">Просмотр</li>
                                            <li class="">
    <a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/?viewer=code" id="tmViewSource" title="Посмотреть исходный текст" rel="nofollow"><span class="fa fa-search"></span> Посмотреть исходный текст</a>
  </li>
        
                  
      <li class="">
    <a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/?viewer=children" id="tmChildren" title="Дочерние страницы" rel="nofollow"><span class="fa fa-folder"></span> Дочерние страницы</a>
  </li>
                  
      <li class="">
    <a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/?viewer=comments" id="tmComment" title="Комментарии" rel="nofollow"><span class="fa fa-comment"></span> Комментарии (0)</a>
  </li>
                    
      <li class="">
    <a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/?viewer=attachments" id="tmAttachments" title="Вложения (2)" rel="nofollow"><span class="fa fa-paperclip"></span> Вложения (2)</a>
  </li>
                  
      <li class="">
    <a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/?viewer=history" id="tmHistory" title="История" rel="nofollow"><span class="fa fa-clock-o"></span> История</a>
  </li>
                  
      <li class="">
    <a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/?viewer=information" id="tmInformation" title="Информация" rel="nofollow"><span class="fa fa-info-circle"></span> Информация</a>
  </li>

<script>
      //<![CDATA[
    /**
     * Perform a PUT on the given REST API. If the request is successful, reload the page.
     *
     * We use this function in order to quickly edit the user properties for developer shortcuts.
     * Also note that JQuery is not supported here, so we use a starndard XMLHttpRequest.
     *
     * @param restUrl the URL to use
     * @param errorMessage the message to display if an error ocurred in the request
     */
    var developerShortcutsRestCall = function(restUrl, errorMessage) {
        const req = new XMLHttpRequest();
        var notification = new XWiki.widgets.Notification(
            "\u0412\u044B\u043F\u043E\u043B\u043D\u0435\u043D\u0438\u0435 REST \u0437\u0430\u043F\u0440\u043E\u0441\u0430...",
            'inprogress');

        req.onreadystatechange = function(event) {
            if (this.readyState === XMLHttpRequest.DONE) {
                if (this.status >= 200 && this.status < 300) {
                    // Reload the page to apply the user modifications
                    notification.replace(new XWiki.widgets.Notification(
                        "REST \u0437\u0430\u043F\u0440\u043E\u0441 \u0432\u044B\u043F\u043E\u043B\u043D\u0435\u043D \u0443\u0441\u043F\u0435\u0448\u043D\u043E!", 'done'));
                    location.reload()
                } else if (this.status == 500) {
                    notification.replace(new XWiki.widgets.Notification(this.data, 'error'));
                } else {
                    notification.replace(new XWiki.widgets.Notification(errorMessage, 'error'));
                }
            }
        };

        req.open('PUT', restUrl, true);
        req.send(null);
    };

    // Append developer shortcuts for toggeling userType and hiddenDocuments in the current user profile
    shortcut.add("x+x+x+a", function() {
        developerShortcutsRestCall("/rest/currentuser/properties/usertype/next",
                "\u041D\u0435\u0432\u043E\u0437\u043C\u043E\u0436\u043D\u043E \u043E\u0431\u043D\u043E\u0432\u0438\u0442\u044C \u0442\u0438\u043F \u0442\u0435\u043A\u0443\u0449\u0435\u0433\u043E \u043F\u043E\u043B\u044C\u0437\u043E\u0432\u0430\u0442\u0435\u043B\u044F");
    }, {'type': shortcut.type.SEQUENCE, 'disable_in_input': true });

    shortcut.add("x+x+x+h", function () {
        developerShortcutsRestCall("/rest/currentuser/properties/displayHiddenDocuments/next",
                "\u041D\u0435\u0432\u043E\u0437\u043C\u043E\u0436\u043D\u043E \u043F\u0435\u0440\u0435\u043A\u043B\u044E\u0447\u0438\u0442\u044C \u0442\u0435\u043A\u0443\u0449\u0435\u0435 \u043F\u043E\u043B\u044C\u0437\u043E\u0432\u0430\u0442\u0435\u043B\u044C\u0441\u043A\u043E\u0435 \u0441\u0432\u043E\u0439\u0441\u0442\u0432\u043E \u0441\u043A\u0440\u044B\u0442\u044B\u0445 \u0434\u043E\u043A\u0443\u043C\u0435\u043D\u0442\u043E\u0432");
    }, {'type': shortcut.type.SEQUENCE, 'disable_in_input': true });
    //]]>
  </script>


                                                        
    <li class="">
    <a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/?viewer=likers" id="likers" title="Просмотреть отметки &quot;Нравится&quot;" rel="nofollow"><span class="fa fa-heart"></span> Просмотреть отметки "Нравится"</a>
  </li>
                        
      </ul>
      </div>
              











          <div class="modal fade text-left" id="exportModal" tabindex="-1" role="dialog" aria-labelledby="exportModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
          <div class="modal-title" id="exportModalLabel">Экспорт</div>
        </div>
        <div class="modal-body">
          <div class="panel-group" id="exportModalAccordion" role="tablist" aria-multiselectable="true">
                          <div class="panel panel-default">
    <div class="panel-heading" role="tab" id="exportModalHeadingOffice">
      <div class="panel-title">
        <a role="button" data-toggle="collapse" data-parent="#exportModalAccordion" href="#exportModelOfficeCollapse" aria-expanded="true" aria-controls="exportModelOfficeCollapse">
          Форматы документов Office
        </a>
      </div>
    </div>
    <div id="exportModelOfficeCollapse" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="exportModalHeadingOffice">
      <div class="panel-body">
        <a href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/?xpage=pdfoptions&amp;qs=" class="btn btn-primary" rel="nofollow">Экспорт в PDF</a>
                  <a href="/bin/export/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome?format=odt" class="btn btn-primary" rel="nofollow">Экспорт в ODT</a>
          <a href="/bin/export/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome?format=rtf" class="btn btn-primary" rel="nofollow">Экспорт в RTF</a>
                      </div>
    </div>
  </div>
              <div class="panel panel-default">
    <div class="panel-heading" role="tab" id="exportModalHeadingOther">
      <div class="panel-title">
        <a class="collapsed" role="button" data-toggle="collapse" data-parent="#exportModalAccordion" href="#exportModalOtherCollapse" aria-expanded="false" aria-controls="exportModalOtherCollapse">
          Другие форматы документов
        </a>
      </div>
    </div>
    <div id="exportModalOtherCollapse" class="panel-collapse collapse" role="tabpanel" aria-labelledby="exportModalHeadingOther">
      <div class="panel-body xform">
                          <p>Выберите страницы для экспорта:</p>
            <div class="export-tree-container">
    <div class="clearfix">
                    <div class="btn-group export-tree-filter pull-left">
    <input type="hidden" name="filter" value="">
    <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      Выбрать:
      <span class="active-filter-title">Все страницы</span>
      <span class="caret"></span>
    </button>
      <ul class="dropdown-menu">
          <li>
        <a href="#" data-filter="installedExtensionDocument">
          <span class="text-success"><span class="fa fa-file-text-o"></span></span>
                              <span class="export-tree-filter-title">Созданные страницы</span>
          <span class="xHint">Страницы, созданные пользователем или расширениями XWiki от имени пользователя.</span>
        </a>
      </li>
          <li>
        <a href="#" data-filter="pristineInstalledExtensionDocument">
          <span class="text-warning"><span class="fa fa-file-code-o"></span></span>
                              <span class="export-tree-filter-title">Созданные и измененные страницы</span>
          <span class="xHint">Включает измененные страницы расширения (обычно страницы конфигурации).</span>
        </a>
      </li>
          <li class="active">
        <a href="#" data-filter="">
          <span class="text-danger"><span class="fa fa-file-o"></span></span>
                                        <span class="export-tree-filter-title">Все страницы</span>
          <span class="xHint">Включает в себя неизмененные страницы расширения.</span>
        </a>
      </li>
      </ul>

  </div>
        <div class="export-tree-actions pull-right">
    <a href="#" class="export-tree-action selectAll btn btn-link">Выбрать всё</a>/<a href="#" class="export-tree-action selectNone btn btn-link">
      -</a>
  </div>
    </div>
                                                                                                                                                                                                          <div class="export-tree jstree-no-links jstree jstree-1 jstree-xwiki jstree-xwiki-responsive jstree-checkbox-selection" data-responsive="true" data-url="/bin/get/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome?outputSyntax=plain&amp;sheet=XWiki.ExportDocumentTree&amp;filterHiddenDocuments=false&amp;showAttachments=false&amp;showTranslations=false&amp;root=document%3Axwiki%3A07%5C.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5.%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC.WebHome&amp;showRoot=true" data-draganddrop="false" data-contextmenu="false" data-icons="true" data-edges="true" data-checkboxes="false" data-opento="" data-finder="false" role="tree" aria-multiselectable="true" tabindex="0" aria-activedescendant="document:xwiki:07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome" aria-busy="false"><ul class="jstree-container-ul jstree-children jstree-contextmenu" role="group"><li role="treeitem" aria-selected="true" aria-level="1" aria-labelledby="document:xwiki:07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome_anchor" id="document:xwiki:07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome" class="jstree-node  jstree-leaf jstree-last"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor  jstree-clicked" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/" tabindex="-1" id="document:xwiki:07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome_anchor"><i class="jstree-icon jstree-checkbox" role="presentation"></i><i class="jstree-icon jstree-themeicon fa fa-file-text-o text-success jstree-themeicon-custom" role="presentation"></i>ЕЖЕНЕДЕЛЬНЫЙ СТАТУС по поставщикам</a></li></ul></div><div class="hidden"></div>
      <dl class="export-tree-legend xHint">
    <dt>Условные обозначения:</dt>
    <dd></dd>
    <dt class="text-success"><span class="fa fa-file-text-o"></span></dt>
    <dd>Созданная страница</dd>
    <dt class="text-warning"><span class="fa fa-file-code-o"></span></dt>
    <dd>Модифицированная страница расширения</dd>
    <dt class="text-danger"><span class="fa fa-file-o"></span></dt>
    <dd>Чистая страница расширения</dd>
  </dl>
  </div>
                <div class="export-buttons">
          <a href="/bin/export/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome?format=html" class="btn btn-primary" rel="nofollow">Экспорт в HTML</a>
                            </div>
      </div>
    </div>
  </div>
          </div>
        </div>
      </div>
    </div>
  </div>
            
              

      </div>




















    </div>
  </div>
<hr>

            
        <div class="row">
    <div id="xwikicontent" class="col-xs-12">
              <table><tbody><tr><th style="text-align: center; background-color: rgb(0, 191, 255); width: 48px;" scope="col"><strong>№</strong></th><th style="width: 174px; text-align: center; background-color: rgb(0, 191, 255);" scope="col"><strong>Поставщик</strong></th><th style="width: 250px; text-align: center; background-color: rgb(0, 191, 255);" scope="col"><strong>Наименование сервиса</strong></th><th style="width: 131px; text-align: center; background-color: rgb(0, 191, 255);" scope="col"><strong>Вид сервиса</strong></th><th style="width: 325px; text-align: center; background-color: rgb(0, 191, 255);" scope="col"><strong>Краткое описание сервиса</strong></th><th style="text-align: center; width: 486px; background-color: rgb(0, 191, 255);" scope="col"><strong>Статус включения</strong></th><th style="text-align: center; width: 81px; background-color: rgb(0, 191, 255);" scope="col"><strong>Квартал включения</strong></th><th style="text-align: center; width: 98px; background-color: rgb(0, 191, 255);" scope="col"><strong>Письмо запрос включения</strong></th><th style="text-align: center; width: 98px; background-color: rgb(0, 191, 255);" scope="col">Декларация и Документация</th><th style="text-align: center; width: 84px; background-color: rgb(0, 191, 255);" scope="col"><strong>Приоритет</strong></th></tr><tr><td colspan="10" style="width:48px">1-й Квартал включения</td></tr><tr><td style="width:48px"><div><p>1</p></div></td><td style="width:174px">ПАО «Сбербанк»</td><td style="width:250px">SDP Analytics</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Подсистема для анализа и визуализации данных в Sber Data Platform</td><td style="width:486px"><div><p>Получен запрос на включение.<br>Провели проверку тех.требований.<br>Подписан протокол проверки, включая тех.долг с планом доработки до конца 2022 г.<br>Документарная проверка в процессе.<br>Выская готовность к включению</p><p>22.12.2022 были направлены все документы для юридической проверки поставщика и документов на сервис<br>23.12.2022 повторная проверка на устранение техдолга</p><p>26.12.2022 в Аппарат Правительства направлено письмо о возможности включения сервиса в каталог ГосТех</p></div></td><td style="width:81px">1</td><td style="width:98px">Да</td><td style="width:98px">&nbsp;</td><td style="width:84px">1</td></tr><tr><td style="width:48px"><div><p>2</p></div></td><td style="width:174px"><div><p>ООО "Квантом"</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">СУБД "Квант-Гибрид"</td><td style="width:131px">Базовый сервис</td><td style="width:325px">Гибридная объектно-реляционная система управления базами с шифрованием</td><td style="width:486px"><div><p>Ожидаемые сроки технической готовности 2023 г.<br>В настоящий момент проходят сертификацию ФСТЭК.<br><br>Планируемое завершение процедуры сертификации февраль 2023.</p><p>Проблема:</p><p>Ограничение ресурсов</p></div></td><td style="width:81px">2</td><td style="width:98px">Да</td><td style="width:98px">&nbsp;</td><td style="width:84px">2</td></tr><tr><td style="width:48px">3</td><td style="width:174px">ООО «Новые Облачные Технологии» (МойОфис)</td><td style="width:250px">"МойОфис Комплект средств разработки (SDK)" в составе Автономного модуля редактирования</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Встраиваемый в браузер модуль редактирования документов, таблиц и презентаций</td><td style="width:486px"><div><p>Проведена документарная проверка.<br>Технические проверки к данному виду продукта не применимы, основываясь на его архитектуре встраивания.<br>Высокая готовность к включению.</p><p>Получены от Поставщика требования на базовые сервисы</p></div></td><td style="width:81px">3</td><td style="width:98px">Да</td><td style="width:98px">&nbsp;</td><td style="width:84px">1</td></tr><tr><td style="width:48px">4</td><td colspan="1" rowspan="2" style="width:174px"><div><p>ООО "БПС Инновационные программные решения"</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">СмартВиста Бэк Офис Рус</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Безопасная система управления платежами</td><td colspan="1" rowspan="2" style="width:486px">Проведена проверка сервиса.&nbsp;&nbsp;<br>Подписан протокол проверки<br><br>30.12.2022 направлен запрос на предоставление Декларации и &nbsp;информации для юридической проверки поставщика и документарной проверки ЦП</td><td colspan="1" rowspan="2" style="width:81px">2</td><td colspan="1" rowspan="2" style="width:98px">Да</td><td rowspan="2" style="width:98px">&nbsp;</td><td colspan="1" rowspan="2" style="width:84px">2</td></tr><tr><td style="width:48px">5</td><td style="width:250px">СмартВиста Интеграционная Платформа (SVIP)</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Интеграция разных информационных систем в едином пространстве</td></tr><tr><td style="width:48px">6</td><td style="width:174px"><div><p>АО "Мой спорт"</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">АИС "Мой спорт"</td><td style="width:131px">SaaS</td><td style="width:325px">Автоматизация работы спортивных организаций и органов власти в сфере физкультуры и спорты</td><td style="width:486px"><div><p>Проведена проверка сервиса.&nbsp;&nbsp;<br>Подписан протокол проверки.</p><p>Открытые вопросы на 19.01.2023<br>1. Готовность авторизации ЕСИА для всех пользователей Сервиса<br>Блокер: Аттестация модуля Crypto.Pro под требования ФСБ, для использования при интеграции с ЕСИА. Предварительный срок март/май 2023<br>2. Аттестация ИБ под К2. Предварительный срок март 2023<br>3. Решить вопрос с ГЧП. Предварительный срок февраль 2023<br>4. Для доработки требования JAM нужны стенды с Платформой (срок предоставления пока не известен, задача на мобильной команде). Предварительный срок февраль-март 2023<br>5. Доработка документации (ТРД на Сервис, отв. Коробков)<br>5.1 Ответ от ФКУ о необходимости сайзинга при размещении на своей инфраструктуре (вопрос входит в ТРД). Предварительный срок март 2023</p></div></td><td style="width:81px">2</td><td style="width:98px">Да</td><td style="width:98px">&nbsp;</td><td style="width:84px">1</td></tr><tr><td style="width:48px">7</td><td style="width:174px"><div><p>ООО «Постгрес Профессиональный»</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">СУБД "PosrgresPro"</td><td style="width:131px">Базовый сервис</td><td style="width:325px">Максимально распространенная в корп.сегменте версия СУБД PostgreSQL</td><td style="width:486px">Проведена проверка сервиса.&nbsp;&nbsp;<br>Подписан протокол проверки.<br><br>17.01.2023 направлен запрос на предоставление Декларации и &nbsp;информации для юридической проверки поставщика и документарной проверки ЦП</td><td style="width:81px">1</td><td style="width:98px">Да</td><td style="width:98px">&nbsp;</td><td style="width:84px">1</td></tr><tr><td style="width:48px">8</td><td style="width:174px">ООО «В КОНТАКТЕ»</td><td style="width:250px">СУБД "Tarantool"</td><td style="width:131px">-</td><td style="width:325px">Платформа in-memory вычислений с гибкой схемой данных для эффективного создания высоконагруженных приложений</td><td style="width:486px">Готовность к демонстрации технической готовности - январь 2023 г.</td><td style="width:81px">3</td><td style="width:98px">Да</td><td style="width:98px">&nbsp;</td><td style="width:84px">2</td></tr><tr><td style="width:48px">9</td><td style="width:174px"><div><p>ООО «1С»</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">Платформа 1С:Предприятие 8.3</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Решение для автоматизации деятельности больниц, клиник, диспансеров различных специализаций</td><td style="width:486px">В процессе развертывание сервиса на предоставленном Сбером стенде для тестирования и доработки.<br>План готовности - I кв. 2023.<br><br>В соответствии с пунктом 9 поручения оперштаба от 16.01.2023 готовятся предложения о включении продуктов "1С" в перечень базовых сервисов.</td><td style="width:81px">1</td><td style="width:98px">&nbsp;</td><td style="width:98px">&nbsp;</td><td style="width:84px">2</td></tr><tr><td style="width:48px">10</td><td style="width:174px">АО "ПФ "СКБ КОНТУР""</td><td style="width:250px">"Сервис видеоконференций"</td><td style="width:131px">SaaS</td><td style="width:325px">Быстрое и безопасное общение в формате видео и аудио конференций</td><td style="width:486px">21.12.2022 проведена проверка сервиса на соответствие МР под протокол с фиксацией техдолга.</td><td style="width:81px">2</td><td style="width:98px">&nbsp;</td><td style="width:98px">&nbsp;</td><td style="width:84px">1</td></tr><tr><td style="width:48px">11</td><td colspan="1" rowspan="2" style="width:174px"><div><p>ООО "АренаДата"</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">Arenadata Analytical DB</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">СУБД аналитического хранилища данных</td><td colspan="1" rowspan="2" style="width:486px">В плане развертывание на стендах Сбера для тестирования совместимости с платформой.<br>Прямое взаимодействие Поставщика со Сбером.<br><br>19.01.2023 направлен запрос на предоставление Декларации и &nbsp;информации для юридической проверки поставщика и документарной проверки ЦП</td><td colspan="1" rowspan="2" style="width:81px">1</td><td colspan="1" rowspan="2" style="width:98px">Да</td><td rowspan="2" style="width:98px">&nbsp;</td><td colspan="1" rowspan="2" style="width:84px">2</td></tr><tr><td style="width:48px">12</td><td style="width:250px">Arenadata Hadoop Platform</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Ширококолоночная (реестровая) СУБД</td></tr><tr><td style="width:48px">13</td><td style="width:174px"><div><p>ООО «Пикодата»</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">Picodata</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Key-value СУБД (in-memory)</td><td style="width:486px">В плане развертывание на стендах Сбера для тестирования совместимости с платформой.<br>Прямое взаимодействие Поставщика со Сбером.<br><br>19.01.2023 направлен запрос на предоставление Декларации и &nbsp;информации для юридической проверки поставщика и документарной проверки ЦП</td><td style="width:81px">1</td><td style="width:98px">&nbsp;</td><td style="width:98px">&nbsp;</td><td style="width:84px">2</td></tr><tr><td style="width:48px">14</td><td style="width:174px"><div><p>ООО «ДАТАМАРТ»</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">Программа оркестрации компонентов витрин данных Datamart Studio</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Обеспечивает управление конфигурацией компонентов витрины данных из визуального интерфейса, эффективное разворачивание витрин и мониторинг всех компонентов после разворачивания и настройки</td><td style="width:486px">19.01.2023 направлен запрос на предоставление Декларации и &nbsp;информации для юридической проверки поставщика и документарной проверки ЦП</td><td style="width:81px">2</td><td style="width:98px">&nbsp;</td><td style="width:98px">&nbsp;</td><td style="width:84px">2</td></tr><tr><td style="width:48px">15</td><td style="width:174px"><div><p>ООО «Бюджетные и Финансовые Технологии»</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">Система «Единая система управления нормативно-справочной информацией БФТ.ЕНСИ»</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Централизованное управление НСИ и мастер-данными</td><td style="width:486px">19.01.2023 направлен запрос на предоставление Декларации и &nbsp;информации для юридической проверки поставщика и документарной проверки ЦП</td><td style="width:81px">2</td><td style="width:98px">Да</td><td style="width:98px">&nbsp;</td><td style="width:84px">2</td></tr><tr><td style="width:48px">16</td><td style="width:174px"><div><p>ООО «Клин дейта»</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">Сервис "Гражданский фактор" модуль "Предиктивный ввод"</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Сервис очистки, стандартизации и формирования эталонного профиля физических и юридических лиц</td><td style="width:486px">Проведена проверка сервиса.&nbsp;&nbsp;<br>Подписан протокол проверки.<br><br>27.12.2022 направлен запрос на предоставление Декларации и &nbsp;информации для юридической проверки поставщика и документарной проверки ЦП</td><td style="width:81px">1</td><td style="width:98px">Да</td><td style="width:98px">&nbsp;</td><td style="width:84px">2</td></tr><tr><td style="width:48px">17</td><td style="width:174px">ООО "Полиматика Рус"</td><td style="width:250px">Polymatica Business Intelligence</td><td style="width:131px">SaaS</td><td style="width:325px">Аналитическая платформа</td><td style="width:486px">29.12.2022 была направлена первая версия ПМИ для проведения проверки, на которую 09.01.2023 были выданы замечания</td><td style="width:81px">2</td><td style="width:98px">Да</td><td style="width:98px">&nbsp;</td><td style="width:84px">2</td></tr><tr><td style="width:48px">18</td><td style="width:174px"><div><p>ООО "Платформа"</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">Энергия данных</td><td style="width:131px">SaaS</td><td style="width:325px">Платформа сбора и анализа данных</td><td style="width:486px">Проведена проверка сервиса.&nbsp;&nbsp;<br>Подписан протокол проверки.<br><br>29.12.2022 направлен запрос на предоставление информации для юридической проверки поставщика и документарной проверки ЦП</td><td style="width:81px">1</td><td style="width:98px">Да</td><td style="width:98px">Получена</td><td style="width:84px">2</td></tr><tr><td style="width:48px">19</td><td colspan="1" rowspan="7" style="width:174px">ООО "Ред Софт"</td><td style="width:250px">«РЕД ОС»</td><td style="width:131px">-</td><td style="width:325px">Операционная система</td><td colspan="1" rowspan="7" style="width:486px">19.12.2022 была направлена информация относительно продуктов для включния, с указанием что часть продуктов готова к проверке уже с 20.12.2022.<br>20.12.2022 в сторону Ред Софт был направлен запрос на предоставление всех документов, необходимых для проведения процедуры включения сервисов в каталог ГосТех.<br>21.12.2022 от Ред Софт были получены скан-копии всех документов по указанным сервисам.<br>Даты проверки сервисов на соответствие методическим рекомендациям на текущий момент не назначены.</td><td colspan="1" rowspan="7" style="width:81px">2</td><td colspan="1" rowspan="7" style="width:98px">Да</td><td rowspan="7" style="width:98px">&nbsp;</td><td colspan="1" rowspan="7" style="width:84px">2</td></tr><tr><td style="width:48px">20</td><td style="width:250px">СУБД «Ред База Данных»</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Система управления базами данных</td></tr><tr><td style="width:48px">21</td><td style="width:250px">Ред Платформа</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Микросервисная платформа</td></tr><tr><td style="width:48px">22</td><td style="width:250px">РЕДШЛЮЗ</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Автоматизация процессов: предоставление услуг через ЕПГУ, взаимодействия со СМЭВ и других</td></tr><tr><td style="width:48px">23</td><td style="width:250px">Цифровая платформа «Принудительное исполнение»</td><td style="width:131px">SaaS</td><td style="width:325px">Автоматизация процессов организации<br>рассмотрения участками мировых судей дел об административных<br>правонарушениях</td></tr><tr><td style="width:48px">24</td><td style="width:250px">Цифровой сервис «Взыскатель»</td><td style="width:131px">SaaS</td><td style="width:325px">Автоматизированная информационная система электронного взаимодействия с ФССП России</td></tr><tr><td style="width:48px">25</td><td style="width:250px">Система интеллектуальных помощников «Цифровая приемная»</td><td style="width:131px">SaaS</td><td style="width:325px">Решение для автоматизации процесса обработки корреспонденции</td></tr><tr><td style="width:48px">26</td><td colspan="1" style="width:174px"><div><p>OOO "РТС-тендер"</p><p><img src="/bin/download/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome/1674461539617-636.png?width=41&amp;height=41&amp;rev=1.1" height="41" width="41" alt="1674461539617-636.png"></p></div></td><td style="width:250px">Капча</td><td style="width:131px">Сервис вендора (PaaS)</td><td style="width:325px">Полностью автоматизированный публичный тест Тьюринга для разделения людей и компьютеров</td><td colspan="1" style="width:486px">18.01.2023 было проведено совещание по анализу ЦП на удовлетворение требованиям методических рекомендаций по включению.</td><td colspan="1" style="width:81px">&nbsp;</td><td colspan="1" style="width:98px">&nbsp;</td><td style="width:98px">&nbsp;</td><td colspan="1" style="width:84px">&nbsp;</td></tr></tbody></table>
          </div>
  </div>
</div>





    <div class="clearfloats"></div>
  </div>            <div id="xdocFooter">
                  <div class="like-container">
<input id="is-liked" type="hidden" value="false">
<div class="like-button btn btn-primary  badge" title="Нажмите, чтобы оценить текущую страницу. У этой страницы 0 отметок &quot;Нравится&quot;.">
<span class="fa fa-heart"></span> <span class="like-number">0</span>
</div>
</div>
                  
         <div class="doc-tags" id="xdocTags">
                        Теги:
            </div>
    
                  <div id="xdocAuthors">
<div class="xdocCreation"> Создал(а) <span class="wikilink"><a href="/bin/view/XWiki/prybakov">Петр Рыбаков</a></span> 2023/01/23 07:37<br>
</div>
</div>
              </div>
              <div id="xwikidata">
      
    
              
    
    
    
                        
            
    
    
      

  <div id="docextraanchors">
  <span id="Commentsanchor">&nbsp;</span><span id="Attachmentsanchor">&nbsp;</span><span id="Historyanchor">&nbsp;</span><span id="Informationanchor">&nbsp;</span>  </div>
  <div id="xwikidatacontents">
    <div class="floatcontainer" id="docExtraTabs">
      <ul class="xwikitabbar" id="docExtrasTabsUl">
                  <li id="Commentstab" data-template="commentsinline.vm" class="active">
                        <a id="Commentslink" href="#Comments" rel="nofollow">
              Комментарии  <span class="itemCount">(0)</span>             </a>
          </li>
                  <li id="Attachmentstab" data-template="attachmentsinline.vm">
                        <a id="Attachmentslink" href="#Attachments" rel="nofollow">
              Вложения  <span class="itemCount">(2)</span>             </a>
          </li>
                  <li id="Historytab" data-template="historyinline.vm">
                        <a id="Historylink" href="#History" rel="nofollow">
              История             </a>
          </li>
                  <li id="Informationtab" data-template="informationinline.vm">
                        <a id="Informationlink" href="#Information" rel="nofollow">
              Информация             </a>
          </li>
              </ul>
    </div>
                <div id="docextrapanes" class="">
              <div id="Commentspane" class=""><div id="commentscontent" class="xwikiintracontent">
  <div id="_comments">
  <p class="noitems">Пока нет комментариев для этой страницы</p>

    </div>     <div class="modal fade" id="permalinkModal" tabindex="-1" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">×</button>
          <div class="modal-title">Постоянная ссылка</div>
        </div>
        <div class="modal-body">
          <div class="input-group">
            <div class="input-group-addon"><span class="fa fa-link"></span></div>
            <input type="text" class="form-control" title="Постоянная ссылка">
          </div>
        </div>
        <div class="modal-footer">
          <input type="button" class="btn btn-primary" data-dismiss="modal" value="Перейти по постоянной ссылке">
          <input type="button" class="btn btn-default" data-dismiss="modal" value="Отмена">
        </div>
      </div>
    </div>
  </div>

    <div class="modal fade" id="deleteModal" tabindex="-1" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">×</button>
          <div class="modal-title">Удалить</div>
        </div>
        <div class="modal-body">
          <div>Вы уверены, что хотите удалить этот комментарий?</div>
        </div>
        <div class="modal-footer">
          <input type="button" class="btn btn-danger" value="Удалить" data-dismiss="modal">
          <input type="button" class="btn btn-default" value="Отмена" data-dismiss="modal">
        </div>
      </div>
    </div>
  </div>

</div></div>
              <div id="Attachmentspane" class="hidden empty"></div>
              <div id="Historypane" class="hidden empty"></div>
              <div id="Informationpane" class="hidden empty"></div>
          </div>
                <script>
      var hashviewer = self.document.location.hash.substring(1);
                                                var extraInit = function(){ XWiki.displayDocExtra("Comments", "commentsinline.vm", false) };
                if (hashviewer == "Comments") {
          var extraInit = function(){ XWiki.displayDocExtra("Comments", "commentsinline.vm", true) };
        }
                                if ($("Commentslink") != null) {
          $("Commentslink").href="#Comments";
          Event.observe($("Commentslink"), "click", function(){ XWiki.displayDocExtra("Comments", "commentsinline.vm", false); }, false);
        }
                                if ($("tmShowComments") != null) {
          $("tmShowComments").href="#Comments";
          Event.observe($("tmShowComments"), "click", function(){ XWiki.displayDocExtra("Comments", "commentsinline.vm", true); }, false);
        }
                                if ($("commentsshortcut") != null) {
          $("commentsshortcut").down('a').href="#comments";
          Event.observe($("commentsshortcut"), "click", function(){ XWiki.displayDocExtra("Comments", "commentsinline.vm", true); }, false);
        }
                                                                              if (hashviewer == "Attachments") {
          var extraInit = function(){ XWiki.displayDocExtra("Attachments", "attachmentsinline.vm", true) };
        }
                                if ($("Attachmentslink") != null) {
          $("Attachmentslink").href="#Attachments";
          Event.observe($("Attachmentslink"), "click", function(){ XWiki.displayDocExtra("Attachments", "attachmentsinline.vm", false); }, false);
        }
                                if ($("tmShowAttachments") != null) {
          $("tmShowAttachments").href="#Attachments";
          Event.observe($("tmShowAttachments"), "click", function(){ XWiki.displayDocExtra("Attachments", "attachmentsinline.vm", true); }, false);
        }
                                if ($("attachmentsshortcut") != null) {
          $("attachmentsshortcut").down('a').href="#attachments";
          Event.observe($("attachmentsshortcut"), "click", function(){ XWiki.displayDocExtra("Attachments", "attachmentsinline.vm", true); }, false);
        }
                                                                              if (hashviewer == "History") {
          var extraInit = function(){ XWiki.displayDocExtra("History", "historyinline.vm", true) };
        }
                                if ($("Historylink") != null) {
          $("Historylink").href="#History";
          Event.observe($("Historylink"), "click", function(){ XWiki.displayDocExtra("History", "historyinline.vm", false); }, false);
        }
                                if ($("tmShowHistory") != null) {
          $("tmShowHistory").href="#History";
          Event.observe($("tmShowHistory"), "click", function(){ XWiki.displayDocExtra("History", "historyinline.vm", true); }, false);
        }
                                if ($("historyshortcut") != null) {
          $("historyshortcut").down('a').href="#history";
          Event.observe($("historyshortcut"), "click", function(){ XWiki.displayDocExtra("History", "historyinline.vm", true); }, false);
        }
                                                                              if (hashviewer == "Information") {
          var extraInit = function(){ XWiki.displayDocExtra("Information", "informationinline.vm", true) };
        }
                                if ($("Informationlink") != null) {
          $("Informationlink").href="#Information";
          Event.observe($("Informationlink"), "click", function(){ XWiki.displayDocExtra("Information", "informationinline.vm", false); }, false);
        }
                                if ($("tmShowInformation") != null) {
          $("tmShowInformation").href="#Information";
          Event.observe($("tmShowInformation"), "click", function(){ XWiki.displayDocExtra("Information", "informationinline.vm", true); }, false);
        }
                                if ($("informationshortcut") != null) {
          $("informationshortcut").down('a').href="#information";
          Event.observe($("informationshortcut"), "click", function(){ XWiki.displayDocExtra("Information", "informationinline.vm", true); }, false);
        }
                                            document.observe("dom:loaded", extraInit, false);
    </script>
  </div> </div>  
        </div>  </div><div id="leftPanels" class="panels left panel-width-Medium">
      <div class="panel expanded  "><h1 class="xwikipaneltitle">Меню</h1><div class="xwikipanelcontents"><div class="menu menu-vertical collapsible open">







                                                                                                                                                                                    <div class="xtree jstree jstree-2 jstree-xwiki jstree-xwiki-responsive" data-responsive="true" data-url="/bin/get/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome?outputSyntax=plain&amp;sheet=XWiki.DocumentTree&amp;root=document%3Axwiki%3A%D0%9C%D0%B5%D0%BD%D1%8E.WebHome" data-draganddrop="false" data-contextmenu="false" data-icons="false" data-edges="false" data-checkboxes="false" data-opento="" data-finder="false" role="tree" aria-multiselectable="true" tabindex="0" aria-activedescendant="document:xwiki:Меню.Пространства проектов.WebHome" aria-busy="false"><ul class="jstree-container-ul jstree-children jstree-no-dots jstree-no-icons" role="group"><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:Меню.Пространства проектов.WebHome_anchor" aria-expanded="false" id="document:xwiki:Меню.Пространства проектов.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/%D0%9C%D0%B5%D0%BD%D1%8E/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%B2/" tabindex="-1" id="document:xwiki:Меню.Пространства проектов.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>1. Пространства проектов</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:Меню.2\. О ФКУ ГосТех.WebHome_anchor" id="document:xwiki:Меню.2\. О ФКУ ГосТех.WebHome" class="jstree-node  jstree-leaf"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/%D0%9C%D0%B5%D0%BD%D1%8E/2.%20%D0%9E%20%D0%A4%D0%9A%D0%A3%20%D0%93%D0%BE%D1%81%D0%A2%D0%B5%D1%85/" tabindex="-1" id="document:xwiki:Меню.2\. О ФКУ ГосТех.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>2. О ФКУ ГосТех</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:Меню.3\. Платформа.WebHome_anchor" id="document:xwiki:Меню.3\. Платформа.WebHome" class="jstree-node  jstree-leaf"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/%D0%9C%D0%B5%D0%BD%D1%8E/3.%20%D0%9F%D0%BB%D0%B0%D1%82%D1%84%D0%BE%D1%80%D0%BC%D0%B0/" tabindex="-1" id="document:xwiki:Меню.3\. Платформа.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>3. Платформа</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:Меню.4\. Сотрудникам.WebHome_anchor" id="document:xwiki:Меню.4\. Сотрудникам.WebHome" class="jstree-node  jstree-leaf jstree-last"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/%D0%9C%D0%B5%D0%BD%D1%8E/4.%20%D0%A1%D0%BE%D1%82%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D0%BA%D0%B0%D0%BC/" tabindex="-1" id="document:xwiki:Меню.4\. Сотрудникам.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>4. Сотрудникам</a></li></ul></div></div></div></div>
        <div class="panel expanded PanelsNavigation Navigation"><h1 class="xwikipaneltitle">Навигация</h1><div class="xwikipanelcontents">







                                                                                                                                                                                                  <div class="xtree jstree jstree-3 jstree-xwiki jstree-xwiki-responsive" data-responsive="true" data-url="/bin/get/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/WebHome?outputSyntax=plain&amp;sheet=XWiki.DocumentTree&amp;showAttachments=false&amp;showTranslations=false&amp;exclusions=document%3Axwiki%3A%D0%9C%D0%B5%D0%BD%D1%8E.WebHome&amp;exclusions=document%3Axwiki%3ASandbox.WebHome&amp;exclusions=document%3Axwiki%3AHelp.WebHome&amp;exclusions=document%3Axwiki%3AXWiki.WebHome" data-draganddrop="false" data-contextmenu="false" data-icons="false" data-edges="false" data-checkboxes="false" data-opento="document:xwiki:07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome" data-finder="false" role="tree" aria-multiselectable="true" tabindex="0" aria-activedescendant="document:xwiki:04\.4 Стандарт управления релизами разработки государственных информационных систем и сервисов с использованием ЕЦП «ГосТех».WebHome" aria-busy="false"><ul class="jstree-container-ul jstree-children jstree-no-dots jstree-no-icons" role="group"><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:ГИС ОМС (ФФОМС).WebHome_anchor" aria-expanded="false" id="document:xwiki:ГИС ОМС (ФФОМС).WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/%D0%93%D0%98%D0%A1%20%D0%9E%D0%9C%D0%A1%20%28%D0%A4%D0%A4%D0%9E%D0%9C%D0%A1%29/" tabindex="-1" id="document:xwiki:ГИС ОМС (ФФОМС).WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>01.1 ФОМС (ГИС ОМС)</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:ГИС ФКиС.WebHome_anchor" aria-expanded="false" id="document:xwiki:ГИС ФКиС.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/%D0%93%D0%98%D0%A1%20%D0%A4%D0%9A%D0%B8%D0%A1/" tabindex="-1" id="document:xwiki:ГИС ФКиС.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>01.2 Минспорт (ГИС ФКиС)</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:Росимущество (ФГИАС ЕСУГИ).WebHome_anchor" aria-expanded="false" id="document:xwiki:Росимущество (ФГИАС ЕСУГИ).WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/%D0%A0%D0%BE%D1%81%D0%B8%D0%BC%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20%28%D0%A4%D0%93%D0%98%D0%90%D0%A1%20%D0%95%D0%A1%D0%A3%D0%93%D0%98%29/" tabindex="-1" id="document:xwiki:Росимущество (ФГИАС ЕСУГИ).WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>01.3 Росимущество (ФГИАС ЕСУГИ)</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:ЕЦП &quot;Социальное казначейство&quot;.WebHome_anchor" aria-expanded="false" id="document:xwiki:ЕЦП &quot;Социальное казначейство&quot;.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/%D0%95%D0%A6%D0%9F%20%22%D0%A1%D0%BE%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BA%D0%B0%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%BE%22/" tabindex="-1" id="document:xwiki:ЕЦП &quot;Социальное казначейство&quot;.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>01.4 ПФР (СФР) ("Социальное казначейство")</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:Домен Наука.WebHome_anchor" aria-expanded="false" id="document:xwiki:Домен Наука.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/%D0%94%D0%BE%D0%BC%D0%B5%D0%BD%20%D0%9D%D0%B0%D1%83%D0%BA%D0%B0/" tabindex="-1" id="document:xwiki:Домен Наука.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>01.5 Домен Наука</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:ГК с ПАО &quot;Сбербанк&quot;.WebHome_anchor" aria-expanded="false" id="document:xwiki:ГК с ПАО &quot;Сбербанк&quot;.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/%D0%93%D0%9A%20%D1%81%20%D0%9F%D0%90%D0%9E%20%22%D0%A1%D0%B1%D0%B5%D1%80%D0%B1%D0%B0%D0%BD%D0%BA%22/" tabindex="-1" id="document:xwiki:ГК с ПАО &quot;Сбербанк&quot;.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>01.6. Минцифры (ГК с ПАО Сбербанк)</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:01\.9 ГИС ЛК (РосЛесХоз).WebHome_anchor" aria-expanded="false" id="document:xwiki:01\.9 ГИС ЛК (РосЛесХоз).WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/01.9%20%D0%93%D0%98%D0%A1%20%D0%9B%D0%9A%20%28%D0%A0%D0%BE%D1%81%D0%9B%D0%B5%D1%81%D0%A5%D0%BE%D0%B7%29/" tabindex="-1" id="document:xwiki:01\.9 ГИС ЛК (РосЛесХоз).WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>01.8 РосЛесХоз (ГИС ЛК)</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:01\.9 ГИС ЭПД (МинТранс).WebHome_anchor" aria-expanded="false" id="document:xwiki:01\.9 ГИС ЭПД (МинТранс).WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/01.9%20%D0%93%D0%98%D0%A1%20%D0%AD%D0%9F%D0%94%20%28%D0%9C%D0%B8%D0%BD%D0%A2%D1%80%D0%B0%D0%BD%D1%81%29/" tabindex="-1" id="document:xwiki:01\.9 ГИС ЭПД (МинТранс).WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>01.9 МинТранс (ГИС ЭПД)</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:02\.1\. Осуществление закупки услуг по обеспечению функционирования, администрирования и бесперебойной работы платформы разработки .WebHome_anchor" aria-expanded="false" id="document:xwiki:02\.1\. Осуществление закупки услуг по обеспечению функционирования, администрирования и бесперебойной работы платформы разработки .WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/02.1.%20%D0%9E%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%BA%D1%83%D0%BF%D0%BA%D0%B8%20%D1%83%D1%81%D0%BB%D1%83%D0%B3%20%D0%BF%D0%BE%20%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8E%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%2C%20%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%B8%20%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%80%D0%B5%D0%B1%D0%BE%D0%B9%D0%BD%D0%BE%D0%B9%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B%20%D0%BF%D0%BB%D0%B0%D1%82%D1%84%D0%BE%D1%80%D0%BC%D1%8B%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20/" tabindex="-1" id="document:xwiki:02\.1\. Осуществление закупки услуг по обеспечению функционирования, администрирования и бесперебойной работы платформы разработки .WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>02.1. Обеспечение предоставления платформы </a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:04\.2 PaaS.WebHome_anchor" aria-expanded="false" id="document:xwiki:04\.2 PaaS.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/04.2%20PaaS/" tabindex="-1" id="document:xwiki:04\.2 PaaS.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>04.2 PaaS</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:4\.2 Методические рекомендации по включению сервисов в ЕЦП &quot;ГосТех&quot;.WebHome_anchor" aria-expanded="false" id="document:xwiki:4\.2 Методические рекомендации по включению сервисов в ЕЦП &quot;ГосТех&quot;.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/4.2%20%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8%20%D0%BF%D0%BE%20%D0%B2%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D1%8E%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BE%D0%B2%20%D0%B2%20%D0%95%D0%A6%D0%9F%20%22%D0%93%D0%BE%D1%81%D0%A2%D0%B5%D1%85%22/" tabindex="-1" id="document:xwiki:4\.2 Методические рекомендации по включению сервисов в ЕЦП &quot;ГосТех&quot;.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>04.2 SaaS</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:4\.2 Стандарт включения сервисов в ЕЦП «ГосТех».WebHome_anchor" id="document:xwiki:4\.2 Стандарт включения сервисов в ЕЦП «ГосТех».WebHome" class="jstree-node  jstree-leaf"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/4.2%20%D0%A1%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%20%D0%B2%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BE%D0%B2%20%D0%B2%20%D0%95%D0%A6%D0%9F%20%C2%AB%D0%93%D0%BE%D1%81%D0%A2%D0%B5%D1%85%C2%BB/" tabindex="-1" id="document:xwiki:4\.2 Стандарт включения сервисов в ЕЦП «ГосТех».WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>04.2 Стандарт включения сервисов в ЕЦП «ГосТех»</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:PaaS.WebHome_anchor" aria-expanded="false" id="document:xwiki:PaaS.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/PaaS/" tabindex="-1" id="document:xwiki:PaaS.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>04.3 ГосСэйф</a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:4\.3 Методические рекомендации по организации производственного процесса разработки государственных информационных систем и сервисов с использованием ЕЦП «ГосТех».WebHome_anchor" id="document:xwiki:4\.3 Методические рекомендации по организации производственного процесса разработки государственных информационных систем и сервисов с использованием ЕЦП «ГосТех».WebHome" class="jstree-node  jstree-leaf"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/4.3%20%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8%20%D0%BF%D0%BE%20%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8%20%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81%D0%B0%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D1%85%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%20%D0%B8%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BE%D0%B2%20%D1%81%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC%20%D0%95%D0%A6%D0%9F%20%C2%AB%D0%93%D0%BE%D1%81%D0%A2%D0%B5%D1%85%C2%BB/" tabindex="-1" id="document:xwiki:4\.3 Методические рекомендации по организации производственного процесса разработки государственных информационных систем и сервисов с использованием ЕЦП «ГосТех».WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>04.3 МР по организации производственного процесса </a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:04\.4 Стандарт управления релизами разработки государственных информационных систем и сервисов с использованием ЕЦП «ГосТех».WebHome_anchor" id="document:xwiki:04\.4 Стандарт управления релизами разработки государственных информационных систем и сервисов с использованием ЕЦП «ГосТех».WebHome" class="jstree-node  jstree-leaf"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/04.4%20%D0%A1%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%20%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D1%80%D0%B5%D0%BB%D0%B8%D0%B7%D0%B0%D0%BC%D0%B8%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D1%85%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D1%85%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%20%D0%B8%20%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BE%D0%B2%20%D1%81%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC%20%D0%95%D0%A6%D0%9F%20%C2%AB%D0%93%D0%BE%D1%81%D0%A2%D0%B5%D1%85%C2%BB/" tabindex="-1" id="document:xwiki:04\.4 Стандарт управления релизами разработки государственных информационных систем и сервисов с использованием ЕЦП «ГосТех».WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>04.4 Стандарт управления релизами </a></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="document:xwiki:07\. Развитие.WebHome_anchor" aria-expanded="true" id="document:xwiki:07\. Развитие.WebHome" class="jstree-node  jstree-open" aria-busy="false"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/" tabindex="-1" id="document:xwiki:07\. Развитие.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>07. Развитие платформенных сервисов</a><ul role="group" class="jstree-children"><li role="treeitem" aria-selected="false" aria-level="2" aria-labelledby="document:xwiki:07\. Развитие.2\.НПА.WebHome_anchor" aria-expanded="false" id="document:xwiki:07\. Развитие.2\.НПА.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/2.%D0%9D%D0%9F%D0%90/" tabindex="-1" id="document:xwiki:07\. Развитие.2\.НПА.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>2.НПА</a></li><li role="treeitem" aria-selected="false" aria-level="2" aria-labelledby="document:xwiki:07\. Развитие.3\.Переписка.WebHome_anchor" id="document:xwiki:07\. Развитие.3\.Переписка.WebHome" class="jstree-node  jstree-leaf"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/3.%D0%9F%D0%B5%D1%80%D0%B5%D0%BF%D0%B8%D1%81%D0%BA%D0%B0/" tabindex="-1" id="document:xwiki:07\. Развитие.3\.Переписка.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>3.Переписка</a></li><li role="treeitem" aria-selected="false" aria-level="2" aria-labelledby="document:xwiki:07\. Развитие.4\.Документация.WebHome_anchor" aria-expanded="false" id="document:xwiki:07\. Развитие.4\.Документация.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/4.%D0%94%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F/" tabindex="-1" id="document:xwiki:07\. Развитие.4\.Документация.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>4.Документация</a></li><li role="treeitem" aria-selected="false" aria-level="2" aria-labelledby="document:xwiki:07\. Развитие.5\.Архитектура.WebHome_anchor" aria-expanded="false" id="document:xwiki:07\. Развитие.5\.Архитектура.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/5.%D0%90%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%B0/" tabindex="-1" id="document:xwiki:07\. Развитие.5\.Архитектура.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>5.Архитектура</a></li><li role="treeitem" aria-selected="false" aria-level="2" aria-labelledby="document:xwiki:07\. Развитие.6\.Ретроспектива.WebHome_anchor" id="document:xwiki:07\. Развитие.6\.Ретроспектива.WebHome" class="jstree-node  jstree-leaf"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/6.%D0%A0%D0%B5%D1%82%D1%80%D0%BE%D1%81%D0%BF%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%B0/" tabindex="-1" id="document:xwiki:07\. Развитие.6\.Ретроспектива.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>6.Ретроспектива</a></li><li role="treeitem" aria-selected="false" aria-level="2" aria-labelledby="document:xwiki:07\. Развитие.7\.Разное.WebHome_anchor" id="document:xwiki:07\. Развитие.7\.Разное.WebHome" class="jstree-node  jstree-leaf"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/7.%D0%A0%D0%B0%D0%B7%D0%BD%D0%BE%D0%B5/" tabindex="-1" id="document:xwiki:07\. Развитие.7\.Разное.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>7.Разное</a></li><li role="treeitem" aria-selected="false" aria-level="2" aria-labelledby="document:xwiki:07\. Развитие.Еженедельные Протоколы.WebHome_anchor" aria-expanded="false" id="document:xwiki:07\. Развитие.Еженедельные Протоколы.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%B6%D0%B5%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%9F%D1%80%D0%BE%D1%82%D0%BE%D0%BA%D0%BE%D0%BB%D1%8B/" tabindex="-1" id="document:xwiki:07\. Развитие.Еженедельные Протоколы.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>Еженедельные Протоколы с поставщика</a></li><li role="treeitem" aria-selected="true" aria-level="2" aria-labelledby="document:xwiki:07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome_anchor" id="document:xwiki:07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome" class="jstree-node  jstree-leaf"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor jstree-clicked" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%95%D0%96%D0%95%D0%94%D0%9D%D0%95%D0%92%D0%9D%D0%AB%D0%99%20%D0%A1%D0%A2%D0%90%D0%A2%D0%A3%D0%A1%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B0%D0%BC/" tabindex="-1" id="document:xwiki:07\. Развитие.ЕЖЕДНЕВНЫЙ СТАТУС по поставщикам.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>ЕЖЕНЕДЕЛЬНЫЙ СТАТУС по поставщикам</a></li><li role="treeitem" aria-selected="false" aria-level="2" aria-labelledby="document:xwiki:07\. Развитие.Материалы для поставщиков.WebHome_anchor" id="document:xwiki:07\. Развитие.Материалы для поставщиков.WebHome" class="jstree-node  jstree-leaf"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%9C%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D1%8B%20%D0%B4%D0%BB%D1%8F%20%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/" tabindex="-1" id="document:xwiki:07\. Развитие.Материалы для поставщиков.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>Материалы для поставщиков</a></li><li role="treeitem" aria-selected="false" aria-level="2" aria-labelledby="document:xwiki:07\. Развитие.Поставщики.WebHome_anchor" aria-expanded="false" id="document:xwiki:07\. Развитие.Поставщики.WebHome" class="jstree-node  jstree-closed"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%9F%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%B8/" tabindex="-1" id="document:xwiki:07\. Развитие.Поставщики.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>Поставщики и ЦП</a></li><li role="treeitem" aria-selected="false" aria-level="2" aria-labelledby="document:xwiki:07\. Развитие.Список часто задаваемых вопросов от Поставщиков.WebHome_anchor" id="document:xwiki:07\. Развитие.Список часто задаваемых вопросов от Поставщиков.WebHome" class="jstree-node  jstree-leaf jstree-last"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="/bin/view/07.%20%D0%A0%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%20%D1%87%D0%B0%D1%81%D1%82%D0%BE%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D1%85%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D0%BE%D0%B2%20%D0%BE%D1%82%20%D0%9F%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/" tabindex="-1" id="document:xwiki:07\. Развитие.Список часто задаваемых вопросов от Поставщиков.WebHome_anchor"><i class="jstree-icon jstree-themeicon fa fa-file-o jstree-themeicon-custom" role="presentation"></i>Список часто задаваемых вопросов от Поставщиков</a></li></ul></li><li role="treeitem" aria-selected="false" aria-level="1" aria-labelledby="pagination:wiki:xwiki_anchor" id="pagination:wiki:xwiki" class="jstree-node  jstree-leaf jstree-last"><i class="jstree-icon jstree-ocl" role="presentation"></i><a class="jstree-anchor" href="#" tabindex="-1" id="pagination:wiki:xwiki_anchor"><i class="jstree-icon jstree-themeicon fa fa-eye jstree-themeicon-custom" role="presentation"></i>71 подробнее ...</a></li></ul></div></div></div>
        <div class="panel expanded PanelsApplications Applications"><h1 class="xwikipaneltitle">Приложения</h1><div class="xwikipanelcontents"><ul class="applicationsPanel nav nav-pills nav-stacked">
<li>
<a href="/bin/view/Dashboard/" title="Панель управления">
<span class="application-img"><span class="fa fa-th-large"></span></span>
<span class="application-label">Панель управления</span>
</a>
</li>
<li>
<a href="/bin/view/Sandbox/" title="Песочница">
<span class="application-img"><span class="fa fa-coffee"></span></span>
<span class="application-label">Песочница</span>
</a>
</li>
</ul>
<ul class="applicationsPanel applicationsPanelMoreList nav nav-pills nav-stacked">
<li>
<a class="applicationPanelMoreButton" href="/bin/admin/XWiki/XWikiPreferences?editor=globaladmin&amp;section=XWiki.AddExtensions" title="Больше приложений">
<span class="application-img"><span class="fa fa-plus"></span></span>
<span class="application-label">Больше приложений</span>
</a>
<div class="applicationPanelMoreContainer hidden" id="applicationPanelMoreContainer40">
<ul class="nav nav-pills nav-stacked">
<li>
<a href="/bin/view/AppWithinMinutes/" title="Создайте свое собственное приложение!">
<span class="application-img"><span class="fa fa-caret-right"></span></span>
<span class="application-label">Создайте свое собственное приложение!</span>
</a>
</li>
</ul>
</div>
</li>
</ul></div></div>
  </div>

  </div>
<div class="clearfloats"></div>
  </div></div><div id="footerglobal">
  <div id="xwikilicence"></div>
            <div id="xwikiplatformversion">
                    <a href="https://extensions.xwiki.org?id=org.xwiki.platform:xwiki-platform-distribution-war:13.10.4:::/xwiki-commons-pom/xwiki-platform/xwiki-platform-distribution/xwiki-platform-distribution-war">
                XWiki 13.10.4
              </a>
          </div>
  </div>

</div></div>
<form id="export-modal-form" method="post"></form><div class="drawer-overlay-upper drawer-toggle"></div></body>
</html>'''

    def registration_and_load_HTML(self, url, login, password) -> bool:
        try:
            response = requests.post(url, auth=HTTPBasicAuth(login, password))
            status_code = response.status_code
        except:
            status_code = 404

        if status_code == 200:
            self.txt_HTML = response.text
            result = True
        elif status_code == 401:
            print('Не верный логин или пароль')
            result = False
        else:
            print('Ошибка подключения к wiki =', status_code)
            result = False
        return result

    def parse_HTML(self, number_table: int):
        txt = self.txt_HTML

        # Выбор нужной таблицы + обрезка лишнего
        for i in range(number_table - 1):
            txt = txt[txt.find('</table>') + 7:]

        # обрезка текста HTML
        if not number_table - 1:
            txt = txt[txt.find('xwikicontent'):txt.find('</table>')]
        else:
            txt = txt[:txt.find('</table>') + 8]

        # Название таблицы
        if not number_table - 1:
            self.start_name = txt[txt.find('<span>') + 6:txt.find('</span>')]
        else:
            self.start_name = txt[txt.find('<span>') + 8:txt.find('</p>')]
            j = self.start_name
            while '<' in self.start_name and '>' in self.start_name:
                self.start_name = self.start_name[:self.start_name.find('<')] + self.start_name[self.start_name.find('>') + 1:]
            while '&nbsp;' in self.start_name:
                self.start_name = self.start_name[:self.start_name.find('&nbsp;')] + self.start_name[self.start_name.find('&nbsp;') + 7:]

        # деление по строкам
        txt_list = list(txt.split('<tr>'))

        # деление по ячейкам
        for nomber, i in enumerate(txt_list):
            if '</th><th' in i:
                txt_list[nomber] = i.split('</th><th')
            elif '</td><td' in i:
                txt_list[nomber] = i.split('</td><td')

        # добавление заголовка таблицы
        # txt_list = txt_list[1:]

        result = list()

        # чистка текста
        for number_i, i in enumerate(txt_list):
            result.append([])

            # начало ячейки с th
            if i[0][:3] == '<th':
                for number_j, j in enumerate(i):

                    # чистка оглавления
                    j = j[j.find('>') + 1:]

                    # окончательная чистка текста в ячейке от артефактов
                    while '<' in j and '>' in j:
                        j = j[:j.find('<')] + j[j.find('>')+1:]

                    if 'nbsp' in j:
                        j = j[:j.find('nbsp') - 1] + j[j.find('nbsp') + 5:]

                    result[number_i].append(j)

            # начало ячейки с td
            elif i[0][:3] == '<td':

                for nomber_j, j in enumerate(i):

                    # чистка от nbsp
                    if '''px">&nbsp;''' in j:
                        j = ' '

                    # работа с ссылками
                    elif 'href' in j:
                        j = j[j.find('<a ') + 3:j.find('</a>')+1]

                        # добавление листа 3 уровня, где есть ссылки
                        j = [j[j.rfind('>')+1:j.rfind('<')], j[j.find('"')+1: j.rfind('>')-1]]
                    else:
                        j = j[j.find('>')+1:]

                    # переносы текста внутри ячейки
                    while '</p><p>' in j:
                        j = j[:j.find('</p><p>')] + f'\n' + j[j.find('</p><p>')+7:]
                    while '<br/>' in j:
                        j = j[:j.find('<br/>')] + f'\n' + j[j.find('<br/>')+5:]

                    # окончательная чистка текста в ячейке от артефактов
                    while '<' in j and '>' in j:
                        j = j[:j.find('<')] + j[j.find('>')+1:]
                    while 'nbsp' in j:
                        j = j[:j.find('nbsp')-1] + j[j.find('nbsp')+5:]

                    result[number_i].append(j)

        print(f'Таблица сформированна: строк = {len(result)-1}, столбцов = {len(result[1])-1}')

        len_norm = len(result[1])
        for i in range(3, len(result)):
            try:
                pobe = int(result[i][0])
            except:
                while len(result[i]) < len_norm:
                    result[i].insert(0, '')




        self.result = result

    def save_xslx(self, pattern_name: str, save_name: str):

        old_word_book = xlrd.open_workbook(pattern_name, formatting_info=True)
        try:
            pattern = old_word_book.sheet_by_index(1)
        except IndexError:
            pattern = old_word_book.sheet_by_index(0)

        work_book = xlwt.Workbook()
        work_table = work_book.add_sheet('sheet', cell_overwrite_ok=True)

        font = xlwt.Font()
        font.name = 'Times New Roman'

        style = xlwt.XFStyle()
        style.alignment.wrap = 1
        style.alignment.horz = style.alignment.HORZ_LEFT
        style.font = font


        font2 = xlwt.Font()
        font2.name = 'Times New Roman'
        font2.bold = 1

        style2 = xlwt.XFStyle()
        style2.pattern_style = pattern_name
        style2.alignment.horz = style.alignment.HORZ_CENTER
        style2.font = font2

        for number_row, row in enumerate(self.result):
            for number_cell, cell in enumerate(row):

                # если ссылка есть
                if type(cell) == list:
                    work_table.write(number_row, number_cell, cell[0], style)

                # если просто текст
                elif type(cell) == str:
                    work_table.write(number_row, number_cell, cell, style)
                else:
                    print('ошибка типа данных для сохранения')

        # ширина столбцов
        for number, col in pattern.colinfo_map.items():
            work_table.col(number).width = col.width

        # высота строк
        for number, row in pattern.rowinfo_map.items():
            work_table.row(number).height = row.height

        # объединенная строка название таблицы
        try:
            if len(self.start_name) < 1000:
                work_table.write_merge(0, 0, 0, len(self.result[1])-1, self.start_name, style2)

            work_table.write_merge(2, 2, 0, len(self.result[1])-1, self.result[2][0], style2)
        except:
            pass
        work_book.save(save_name)

    def test_print_HTML(self):
        print(self.txt_HTML)

    def test_print_result_no_parse(self, number_table):

        txt = self.txt_HTML

        # Выбор нужной таблицы + обрезка лишнего
        for i in range(number_table - 1):
            txt = txt[txt.find('</table>') + 7:]

        # обрезка текста HTML
        if not number_table - 1:
            txt = txt[txt.find('xwikicontent'):txt.find('</table>')]
        else:
            txt = txt[:txt.find('</table>') + 8]

            # Название таблицы
            if not number_table - 1:
                self.start_name = txt[txt.find('<span>') + 6:txt.find('</span>')]
            else:
                self.start_name = txt[txt.find('<span>') + 8:txt.find('</p>')]
                j = self.start_name
                while '<' in self.start_name and '>' in self.start_name:
                    self.start_name = self.start_name[:self.start_name.find('<')] + self.start_name[
                                                                                    self.start_name.find('>') + 1:]
                while '&nbsp;' in self.start_name:
                    self.start_name = self.start_name[:self.start_name.find('&nbsp;')] + self.start_name[
                                                                                         self.start_name.find(
                                                                                             '&nbsp;') + 7:]

        # деление по строкам
        txt_list = list(txt.split('<tr>'))

        # деление по ячейкам
        for nomber, i in enumerate(txt_list):
            if '</th><th' in i:
                txt_list[nomber] = i.split('</th><th')
            elif '</td><td' in i:
                txt_list[nomber] = i.split('</td><td')

        for i in txt_list:
            print('-'*200)
            for j in i:
                print(j)

    def copy_xls(self, pattern_name: str, save_name: str):

        workbook = xlrd.open_workbook(pattern_name, on_demand=True, formatting_info=True)

        try:
            sheet = workbook.sheet_by_index(1)
        except IndexError:
            sheet = workbook.sheet_by_index(0)

        workbook_update = copy(workbook)  # копировать книгу

        sheet_update = workbook_update.get_sheet(0)
        new_style = workbook.xf_list[0]
        sheet_update.write(0, 0, '1232142345346')
        workbook_update.save(save_name)

    def parse_HTML2(self):
        file = self.txt_HTML

        htmldoc = html.fromstring(file)

        with open("output.xml", 'wb') as out:
            out.write(etree.tostring(htmldoc))





def input_config(data: dict) -> dict:
    dict_config = {
        'login': 'Введите login', 'password': 'Введите пароль', 'url': 'Добавьте адрес Xwiki',
        'pattern_name': 'Введите имя шаблона', 'save_name': 'Введите имя файла для сохранения',
        'number_table': 'Введите номер таблицы для использования'
    }
    for kye, value in dict_config.items():
        if data[kye] == '' or data[kye] == ' ' or data[kye] == None:
            print(value)
            data[kye] = input()
    return data
