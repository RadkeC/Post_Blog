style_nav = """
* {
  margin: 0px 0px;
  padding: 0px 0px;
}
html {
    --color_first: #FDD700; /* menu nav, footer */
    --color_second: #FF0000; /* borders , hoover */
    --color_third: #fcb103; /* background */
    --color_fourth: #FF00FF; /* form border */
    --color_5: #FFFFFF; /* form border */
}

body {
    width:100%;
    height:100%;

    background-color: var(--color_third) !important;
}

/* menu */
.section_nav {
    background-color: var(--color_first);
    width: 100%;
    height:72px;
    position: fixed;
    left: 0;
    top: 0;
    z-index: 100;
}
ol {
    list-style-type:none;
    padding:0;
    margin:0;
    font-size:20px;
    height:60px;
    line-height: 60px;
    text-align:center;
    width:100%;
}
ol > li {
    float:left;
    background-color: var(--color_first);
    width:15%;
}
.li_title {
    padding-top: 10px;
    width: 40%;
    height:72px;
    line-height:1em;
}
.div_title {
    line-height:1em;
    height: 60px;
    margin: 0px;
    padding: 0px;
}
ol a {
  display:block;
  color:#000;
  text-decoration:none;
  padding:0 5px;
}
ol > li {
  border-style: solid;
  border-width: 6px 3px;
  border-color: var(--color_second);
  box-sizing: border-box;
}
ol > li.li_menu:hover {
  color: var(--color_second);
  font-weight: bold;

  border-style: solid;
  border-width: 5px;
  border-color: var(--color_second);
  box-sizing: border-box;
}

/* podmenu */
ol > li > ul {
  list-style-type:none;
  padding:0;
  margin:0;

  display:none;
}
ol > li:hover > ul {
  display:block;
}
ol > li > ul> li > a:hover {
  color: #FF0000;
  font-weight: bold;

  border-style: solid;
  border-width: 6px 0px;
  border-color: var(--color_second);
  box-sizing: border-box;
}
ol > li > ul> li:last-child > a:hover {
  border-width: 6px 0px 0px 0px;
}


/* content */
.section_content {
    margin: 72px 0px 0px 0px;
    padding-top: 0px; /* 300px */
    min-height: calc(100vh - 102px);
    background-color: var(--color_third);
}

/* raport */
.section_raport {
    padding-top: 10px;
    padding-left: 10px;
}

/* footer */
.section_footer {
    height: 30px;
    width: 100%;

    background-color: var(--color_first);
    border: solid;
    border-width: 6px 0px 0px 0px;
    border-color: var(--color_second);
    box-sizing: border-box;
}

.section_footer > p {
    float:right;
    margin-right: 5px;
}

"""