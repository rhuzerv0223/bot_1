import discord
from discord.ext import commands
import bot_1.keep_alive as keep_alive
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
  jdata = json.load(jfile)

bot = commands.Bot(command_prefix='跟風')
  
@bot.command()
async def 排泄(ctx):
   await ctx.send("先從頭開始說吧 我跟他們之前很常玩在一塊 就一起打R6或聊天 直到我們第一次吵架 我們第一次吵架的原因我記得好像是因為我覺得他們玩AmongUs很低能 玩那個幹嘛 他們說我一個人排洩他們玩AmongUs 於是我向他們道歉 你也知道 我平時嘴就很臭 這件事情造就的結果是他們額外創了一個群 和好了之後 我們又繼續都玩在一塊 到了第二次吵架 好像是因為他們不喜歡我在那邊靠北 我爽我在跟風啊 嘴臭啊什麼的 反正他們認為就是我的錯 之後我們幾個就稍微有點分裂 那時候我跟騰祥還有開宇關係也很好阿 那是在吵架的時候 他們兩個是站在我這邊的 會幫我講話 之後又和好了嘛 開學之後我晚上回家都還是會跟開宇騰祥玩麥塊聊天討論功課什麼的 偶爾會去加瑪打台 假日換他們三個 陳新明 斌斌 楊凱閎上線 一起打R6之類的 之前就是他們三個不爽我 第二次段考完後 在這次高中分班之後呢 我跟以前有個三到六年級都同班的朋友再同班一以下簡稱他為男1 因為我高中跟斌斌同班嘛 他就問我們說要不要去他的DC群這樣 之後我們就去了 在一段時間後 我開始漸漸發現 那五個人 開宇 騰祥 斌斌 陳新明 楊凱閎都不太理我 我用messenger問他們訊息他們也都敷衍我 之後的某一個星期天 因為我平常都會嘴臭嘛 我在男1的DC群PO了一個圖 就是我Apex屌打對面的圖 然後男1就問我一些問題 我就回他說 啊我打的模式不一樣啊 用一下你的腦袋好不好 過一段時間後我發現我的留言被刪了 之後我去問男1 他去看審核日誌 發現是斌斌刪的 隔天早上某一節下課的我再次確認是斌斌刪的 我就直接去問他 幹 你為什麼要刪我的留言 你有伺服器的權限就可以這樣亂用嗎 他說 沒啊 啊我就看你不爽在那邊嗆人啊 然後我回說 啊幹 不是欸 我又不是嗆你 我嗆的是男1 我有問過男1當時被我嗆的感覺是甚麼 他說他和好啊他不會怎麼樣 那你憑什麼可以濫用職權 之後我們就互相辯論 但我最後就很不解 也很不爽 我就嗆斌斌好幾句 幹你娘雞掰 之後上課鐘聲響了 然後我們就沒有再說過話 這件事情發生後 我就開始檢討 我是不是哪裡做錯了 我是不是做人很失敗 於是我就去問了其他除了斌斌以外的四個人以及其他我的朋友 他們都說還好只是嘴巴 有時候很賤之類的 我也有去問其他四個人 我跟斌斌吵架了 我現在該怎麼辦 該做什麼才能讓他消氣 過了大概四天左右11月4號晚上 蔡子斌跟蔡騰祥就傳了這個訊息給我 內容是：該攤牌了 其實我們排泄你很長一段時間 大家都很討厭你這種個性 所以今天我們想做個了結 從此斷絕關係 當我知道這件事情的時候簡直晴天霹靂 我當下直接不知所措 後來我告知了陳新明這件事情他也有安慰我 說我嘴臭的程度以及吵架的過程傷到斌斌的自尊 下群朋友可能會更好 我也有去問開宇 他只說了簡短的一句話 “事不過三” 後來我去問我的閨蜜 她也跟我說了關於她之前跟朋友吵架的故事 也告訴我該怎麼處理 也修正了我那個過於草率的道歉信 也告訴了我很多這方面的經驗及領悟 所以我也很謝謝她 之後我寫好了道歉信 隔天早上買了巧克力 把巧克力跟信都放在他的桌上 我也有目睹他看到這信的畫面 他好像有把整張信看完 不過巧克力後來就送給我同學了 之後我們之間就再也沒什麼交集 男1在學校的時候跟蔡子斌是比較親密的 所以我會去問男1說 你們今天聊了什麼 有聊到我嗎之類的 到了現在我也頂多跟陳新明楊凱閎在messenger聊些天 問一些問題")
    
@bot.command()
async def 開宇騰祥(ctx):
  await ctx.send("那時候我跟騰祥還有開宇關係也很好阿 那是在吵架的時候 他們兩個是站在我這邊的 會幫我講話")
  
@bot.command()
async def 跟風(ctx):
   await ctx.send("我爽我在跟風啊")
  
@bot.command()
async def 朋友(ctx):
   await ctx.send("朋友是一个坚韧不拔的纪录片，在香港这座城市的设置。主演：钱德勒 索罗斯 傅博斯1  瑞秋 莫妮卡 和一些其他他妈的演员。中国是一个解放的国家。中国是一个伟大的国家。中国是一个万物都是完美的国家。中国是我们最接近天堂的地方 不相信我？ 这是为什么。我咳嗽很多，但我不具传染性。政府已经照顾这种病毒非常好。天安门广场什么都没有发生 我们没有被审查。我们可以自由发言了我们喜欢统治者。我们没做错什么我还没有失去我的社会信用。我是社会的一个正常运作的成员。统治者是最伟大的！ 我喜欢统治者 统治者是众所周知的。香港的抗议活动并不存在。每个人都喜欢这个国家！ 包括那些没有经历过我国家充满荣耀的dirty脏外人。我为生活在这个国家感到自豪。我不能离开我的祖国 我是这个国家正常运作的一员，但你是?？我愿意为这个国家牺牲所有的人性我不能说什么不好的关于我的国家，或者我失去我的家人。但我的国家比我的家人更好！我会为这个国家做任何事我为我的国家感到骄傲中国是最重要的！ 我爱你，中国。这不是propoganda，因为我爱中国这么多。 中国第一！")  
  
@bot.command()
async def 神解(ctx):
 await ctx.send("欸你知道嗎 我剛剛啊 直接硬幹欸")

@bot.command()
async def 中二(ctx):
  random_song = random.choice(jdata["song"])
  song = discord.File(random_song)
  await ctx.send(file= song)
  
@bot.command()
async def 射精(ctx):
    await ctx.send('https://yt3.ggpht.com/ytc/AKedOLTugLcdNlcskxg5fD4Uwh4b_x9Ud_Qqi6Tif6Yt6A=s900-c-k-c0x00ffffff-no-rj')
  
@bot.event
async def on_message(message):
      if message.content.startswith('表哥來談條件吧'):
          channel = message.channel
          await channel.send('22:00之後來找我')
          def checkmessage(m):
              return m.content == '表哥？' and m.channel == channel
          msg = await bot.wait_for('message', check=checkmessage)
          await channel.send('需要解釋？？＿請搞清楚'.format(msg))

@bot.event
async def on_meber_join(meber):
  channel = bot.get_channel(904153305645740062)
  await channel.send(F'{meber}看來有人以為可以挽回')

@bot.event
async def on_meber_remove(meber):
  channel = bot.get_channel(904153305645740062)
  await channel.send(F'{meber}自行離開即可')

@bot.event
async def on_ready():
  print('沒有跟風啦',bot.user)
  game = discord.Game('跟風三高雙雄')
  await bot.change_presence(status=discord.Status.idle, activity=game)
  
keep_alive.keep_alive()
bot.run(jdata['TOKEN'])