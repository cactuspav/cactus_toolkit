#python

# set_center_Pos.py
#
# Move the current item's center to selected element Position.
# Created by Cristobal Vila, based on a script by Dongju, shared here:
# http://forums.luxology.com/topic.aspx?f=37&t=37677
#
# Remember and apply previous selection code shared by Dongju, here:
# http://forums.luxology.com/topic.aspx?f=37&t=55579

def selmode(*types):
    if not types:
        types = ('vertex', 'edge', 'polygon', 'item', 'pivot', 'center', 'ptag')
    for t in types:
        if lx.eval('select.typeFrom %s;vertex;edge;polygon;item;pivot;center;ptag ?' %t):
            return t

seltype = selmode()

lx.eval('query sceneservice scene.index ? current')

meshID = lx.evalN('query sceneservice selection ? mesh')[0]

lx.eval('workPlane.fitSelect')

lx.eval('select.center {%s}' %meshID)

lx.eval('center.matchWorkplanePos')

lx.eval('workPlane.reset')

lx.eval('select.type %s' %seltype)