from bs4 import BeautifulSoup as bs


def xml_to_json(sp,sep=""):
    #sp=bs(string,'lxml')
    #print "*********************"
    #print sp
    #print "*********************"
    if "[document]" in sp.name or "body" in sp.name or "html" in sp.name :
        for elm in sp.findChildren(recursive=False):
            xml_to_json(elm,sep)
    else :
        print sep,sp.name
        for elm in sp.findChildren(recursive=False):
            xml_to_json(elm," "*5+sep)
        for elm in sp.attrs :
            print sep,'+++',elm,":",sp[elm]
    #return sp


if __name__=="__main__":
    xml_to_json( bs("""<_frame>
                                <get_users>
			            <data id="0">
				        <item name="terminal" value=":1"/>
				        <item name="started" value="1545214592.0"/>
				        <item name="host" value=":1"/>
				        <item name="pid" value="2267"/>
				        <item name="name" value="root"/>
			            </data>
		                </get_users>
	                </_frame>
""","lxml"))

