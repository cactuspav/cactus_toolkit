#perl
#AUTHOR: Seneca Menard
#version 1.0
#-EDGEWEIGHT_reset: this resets the edge weighting.   ALWAYS GREAT!!!

my $selCount;

if( lxq( "select.typeFrom {vertex;polygon;item;edge} ?" ) ) {
	$selCount = lxq("select.count vertex ?");
}
elsif( lxq( "select.typeFrom {edge;vertex;polygon;item} ?" ) ) {
	$selCount = lxq("select.count edge ?");
}
elsif( lxq( "select.typeFrom {polygon;item;edge;vertex} ?" ) ) {
	$selCount = lxq("select.count polygon ?");
}

#makes sure you don't accidentally remove all your vertex weighting!
if ($selCount != 0)
{
	lx("select.vertexMap Subdivision subd replace");
	lx("tool.set vertMap.setWeight on");
	lx("tool.setAttr vertMap.setWeight weight [0.0 %]");
	lx("tool.doApply");
	lx("select.nextMode");
}

