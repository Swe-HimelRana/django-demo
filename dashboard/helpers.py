import re

def isMobile(userAgent):
    
    mobiles = [
            "Android",
            "webOS",
            "iPhone",
            "iPad",
            "iPod",
            "BlackBerry",
            "Windows Phone"
        ];
        
    for mobile in mobiles:
      if re.search(mobile, userAgent):
          return True
    return False