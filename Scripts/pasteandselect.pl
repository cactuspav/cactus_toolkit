#perl
#AUTHOR: Seneca Menard
#version 2.0
#This tool is exactly the same as a regular paste only when you paste it'll select what you just pasted.  VERY handy!  :)

#6-27-10 : put in a small speed increase for the later versions of modo.

my $modoVer = lxq("query platformservice appversion ?");


if ($modoVer > 301){
	lx("!!select.all");
	lx("!!select.paste");
	lx("!!select.invert");
}else{
	if		( lxq( "select.typeFrom {edge;vertex;polygon;item} ?" ) )	{lx("!!select.drop edge");	}
	elsif	( lxq( "select.typeFrom {polygon;vertex;edge;item} ?" ) )	{lx("!!select.drop polygon");	}
	else																{lx("!!select.drop vertex");	}

	lx("!!select.invert");
	lx("!!select.paste");
	lx("!!select.invert");
}
