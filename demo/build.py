# -*- coding: utf-8 -*-
"""拆出 5 张独立幻灯片，并生成带版面审计脚本的检查版。"""
import re, io

SRC = "preview.html"
src = open(SRC, encoding="utf-8").read()
css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)

AUDIT = r"""
<script>
(function(){
  var slide = document.querySelector('.slide');
  var srect = slide.getBoundingClientRect();
  var out = [];
  var svgns = 'http://www.w3.org/2000/svg';
  var els = slide.querySelectorAll('*');
  var skip = ['pg', 'ring', 'deco', 'corner'];
  function hasSkip(el) {
    var c = (el.className && el.className.baseVal !== undefined) ? el.className.baseVal : (el.className || '');
    return skip.some(function (k) { return c.indexOf(k) > -1; });
  }
  for (var i = 0; i < els.length; i++) {
    var el = els[i];
    if (el.namespaceURI === svgns) continue;
    if (hasSkip(el)) continue;
    var r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    if (r.left < srect.left - 4 || r.right > srect.right + 4 ||
        r.top < srect.top - 4 || r.bottom > srect.bottom + 4) {
      out.push('OUTSIDE:' + el.tagName + '.' + el.className + ' rect=' + Math.round(r.left) + ',' + Math.round(r.top) + ',' + Math.round(r.right) + ',' + Math.round(r.bottom));
    }
    var boxy = /tbox|imgcard|sitem|comic|smart|hd|txt|pic/.test(el.className || '');
    if (boxy && el.scrollHeight > el.clientHeight + 4 && el.clientHeight > 0) {
      out.push('V-OVERFLOW:' + el.tagName + '.' + el.className + ' sh=' + el.scrollHeight + ' ch=' + el.clientHeight);
    }
  }
  var pre = document.createElement('pre');
  pre.id = 'AUDIT';
  pre.textContent = out.length ? out.join('\n') : 'AUDIT_OK';
  document.body.appendChild(pre);
})();
</script>
"""

for n in range(1, 6):
    m = re.search(r'<section class="slide" id="p%d">(.*?)</section>' % n, src, re.S)
    assert m, "section p%d not found" % n
    inner = m.group(1)
    for name, extra in (("slide%d.html" % n, ""), ("slide%d_check.html" % n, AUDIT)):
        html = ('<!doctype html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
                '<style>' + css + '</style>\n</head>\n<body style="margin:0">\n'
                '<section class="slide" id="p%d">%s</section>\n%s\n</body>\n</html>' % (n, inner, extra))
        with io.open(name, "w", encoding="utf-8") as f:
            f.write(html)
    print("p%d ok" % n)