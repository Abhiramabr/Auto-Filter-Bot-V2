class script(object):


    START_MSG = """ <b>Hi {}

I'm Just A Simple Auto Filter Bot! Bot For Searching Files From Channel...

Just Sent Any Text I Will Search In All Connected Chat And Reply You With The Message link

You Can Even Connect 3 Channels At A Time...

For more click <i>help</i></b>"""


    HELP_MSG = """<b>How to use the bot??</b>

<i>
* Add bot to your group with admin rights.

* Add bot to channels which you want to link with <b>all admin rights</b>!
</i>


<b>Bot Commands - Works in Group only</b>
(You need to be a Auth User in order to use these commands)

* <code>/add channelid</code>  -  Links channel to your group.
or
* <code>/add @channelusername</code> - Links channel to your group.

<i>NOTE : You can get your channel ID from @ChannelidHEXbot </i>


* <code>/del channelid</code>  -  Delinks channel from group
or
* <code>/del @channelusername</code>  -  Delinks channel from group

<i>NOTE : You can get connected channel details by <code>/filterstats</code> </i>


* <code>/delall</code>  -  Removes all connected channels and filters from group!

<i>Note : Dont add command delete bots in group! Otherwise, delall command wont work</i>


* <code>/filterstats</code>  -  Check connected channels and number of filters.



No need add each filter again!
Bot will automatically search for your files and give links to that!

"""


    ABOUT_MSG = """I'm an auto filter bot!\n

I can pick the files/videos from the channel and send it in your group as buttons!

"""
