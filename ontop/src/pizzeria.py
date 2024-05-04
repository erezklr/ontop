from IPython.core.display import HTML
import datetime
from IPython.display import clear_output
import random

#########################################################
def input_number(msg):
  return int(input(msg))
#########################################################


# ===========================
# "run me" strip
# ===========================
banners = ["https://data.cyber.org.il/OnTop/GifBanner/colab_celebrate_1.gif",
           "https://data.cyber.org.il/OnTop/GifBanner/colab_celebrate_2.gif",
           "https://data.cyber.org.il/OnTop/GifBanner/colab_celebrate_3.gif",
           "https://data.cyber.org.il/OnTop/GifBanner/colab_celebrate_4.gif"]
greetings=["יש! סיימתי שלב",
           "איזה כיף, סיימתי את השלב",
           "כל הכבוד לי! סיימתי עוד שלב",
           " :)סיימתי שלב, מגיעה לי הפסקה",
           "אליפות! סיימנו עוד משימה",
           "נהדר! זה כבר כמעט הסוף",
           "ישששששששששששש"]

def run_me(greetings_num=-1):
  banner_num = random.randint(0, 3)
  if greetings_num == -1:
    greetings_num = random.randint(0, 4)
  #print(banner_num)
  #print(greetings_num)
  html = '''
  <svg width="970"  style="background-color:aliceblue">
   <image href={banner} />
   <defs>
    <filter id="f3" x="0" y="0" width="100%" height="100%">
      <feOffset result="offOut" in="SourceAlpha" dx="0" dy="0" />
      <feGaussianBlur result="blurOut" in="offOut" stdDeviation="10" />
      <feBlend in="SourceGraphic" in2="blurOut" mode="normal" />
    </filter>
  </defs>
   <text x="50%" y="80" dominant-baseline="middle" text-anchor="middle" font-size="30" fill="#1F33BE" font-weight="bold" filter="url(#f3)">{*}</text>
   <text x="50%" y="45" dominant-baseline="middle" text-anchor="middle" font-size ="20" fill="#1F33BE"  filter="url(#f3)">{date}</text>
 </svg>
'''

#<rect x="40%" y="60" width="250" height="40" fill="red"/>
  today = datetime.date.today()
  html = html.replace("{*}", greetings[greetings_num])
  html = html.replace("{date}", str(today.day) + "." +  str(today.month) + "." +  str(today.year))
  html = html.replace("{banner}", banners[banner_num])

  display(HTML(html))