#python

# cheapNormalExtrude.py by Shaun Absher
# Shared here: http://forums.luxology.com/topic.aspx?f=119&t=76390

lx.eval('edge.growQuads true 1.0 89.9 false')
lx.eval('edge.growQuads true 1.0 89.9 false')
lx.eval('select.convert vertex')
lx.eval('select.expand')
lx.eval('select.convert polygon')
lx.eval('select.expand')
lx.eval('tool.set poly.bevel on')
lx.eval('tool.attr poly.bevel edges inner')
lx.eval('tool.attr poly.bevel shift 0.1')
lx.eval('tool.attr poly.bevel srand 0.0')
lx.eval('tool.attr poly.bevel irand 0.0')
lx.eval('tool.attr poly.bevel inset 0.0')
lx.eval('tool.doApply')
lx.eval('select.typeFrom vertex;edge;polygon;item;pivot;center;ptag true')
lx.eval('select.drop vertex')
lx.eval('select.typeFrom edge;vertex;polygon;item;pivot;center;ptag true')
lx.eval('select.convert vertex')
lx.eval('select.expand')
lx.eval('select.convert polygon')
lx.eval('select.expand')
lx.eval('select.expand')
lx.eval('script.run "macro.scriptservice:92663570022:macro"')
lx.eval('select.typeFrom polygon;edge;vertex;item;pivot;center;ptag true')
lx.eval('delete')
lx.eval('select.typeFrom edge;vertex;polygon;item;pivot;center;ptag true')
lx.eval('tool.set edge.slide on')
