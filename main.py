import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SelectOption, ButtonStyle, ui, Permissions, Embed, TextInputStyle
from nextcord.ui import Button, Modal, TextInput, View, Select
import random
import os
import json
import pytz
import urllib
import requests
import datetime
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from nextcord.utils import get
import time




bot = commands.Bot(command_prefix='a!', intents=nextcord.Intents.all())

token = "MTM3NDE5MzEzMTkxMzg3NTQ3Ng.GByY95.PC3mw2TkBWV58olp0h1raJxXyEonJjHNJcqhi0"

ROLE_ID = 1373721230271578192  # vfy role

log_vfy = 1374192317107273808

log_77 = "🧾︱ข้อมูล"

log_kick = "🧾︱ข้อมูล" #แจ้งเรื้อน

log_out = "🧾︱ข้อมูล"

log_join = "🧾︱ข้อมูล"

log_voice = 1182010203789598741

gu = 1373912396216926268

ch = 1374192317107273808

phocute = 1374217978618581032

log_invite = 1374192317107273808


@bot.event
async def on_ready():
    bot.add_view(Button())
    print(f"บอทออน : {bot.user}")
    await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Game(name="༒ Arcane Domain ༒"))
    


    
    
@bot.event
async def on_voice_state_update(member, before, after):
   
    if after.channel and after.self_stream:
        print(f'{member.name} is in {after.channel.name} and started speaking.')
    


# Event เมื่อมีคนเข้าเซิร์ฟเวอร์
@bot.event
async def on_member_join(member):
    log_channel = nextcord.utils.get(member.guild.channels, name=log_join)
    
    if log_channel:
        embed = nextcord.Embed(
            description=f"> **ยินดีต้อนรับ {member.mention} เข้าสู่เซิร์ฟเวอร์ **<a:jungwad_anime:1297070556419592202>",
            color=0x3151F7
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.add_field(name="**ชื่อผู้ใช้**", value=member.name, inline=True)
        embed.add_field(name="**ID ผู้ใช้**", value=str(member.id), inline=True)
        embed.set_footer(text=f"สมาชิกเข้ามาวันที่: {member.joined_at}")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1297759703270690816/1297960070147080254/IMG_1045.jpg?ex=6717d303&is=67168183&hm=32dfed5a213192b1fc1d6157deede48a3a4fb3f7835d8bfd93b1ac526261956d&")
        
        await log_channel.send(embed=embed)

# Event เมื่อมีคนออกจากเซิร์ฟเวอร์
@bot.event
async def on_member_remove(member):
    log_channel = nextcord.utils.get(member.guild.channels, name=log_out)
    
    if log_channel:
        embed = nextcord.Embed(
            description=f"> **{member.mention} ได้ออกจากเซิร์ฟเวอร์แล้วกั้บ**",
            color=0x3151F7
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.add_field(name="**ชื่อผู้ใช้**", value=member.name, inline=True)
        embed.add_field(name="**ID ผู้ใช้**", value=str(member.id), inline=True)
        embed.set_footer(text=f"สมาชิกออกวันที่: {nextcord.utils.utcnow()}")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1297759703270690816/1297960070147080254/IMG_1045.jpg?ex=6717d303&is=67168183&hm=32dfed5a213192b1fc1d6157deede48a3a4fb3f7835d8bfd93b1ac526261956d&")
        
        await log_channel.send(embed=embed)

        
########]#]#]##]#]#]#]##]]#]##]

@bot.event
async def on_voice_state_update(member, before, after):
    # ดึง channel ที่จะแจ้งเตือน
    log_channel = bot.get_channel(log_voice)  # ใช้ log_voice แทน

    # กรณีผู้ใช้เข้าช่องเสียง
    if before.channel is None and after.channel is not None:
        embed = nextcord.Embed(
            title="> มีคนเข้าข่องเสียง",
            description=f"> **{member.name} เข้าช่องเสียง {after.channel.name}**",
            color=nextcord.Color.green()
        )
        embed.set_thumbnail(url=member.avatar.url)  # ตั้งรูปโปรไฟล์ของผู้ใช้ใน embed
        await log_channel.send(embed=embed)

    # กรณีผู้ใช้ออกจากช่องเสียง
    elif before.channel is not None and after.channel is None:
        embed = nextcord.Embed(
            title="> มีคนออกจากช่องเสียง",
            description=f"> **{member.name} ออกจากช่องเสียง {before.channel.name}**",
            color=nextcord.Color.red()
        )
        embed.set_thumbnail(url=member.avatar.url)
        await log_channel.send(embed=embed)

    # กรณีผู้ใช้ย้ายจากช่องเสียงหนึ่งไปยังอีกช่องหนึ่ง
    elif before.channel is not None and after.channel is not None and before.channel.id != after.channel.id:
        embed = nextcord.Embed(
            title="> มีคนย้ายช่องเสียง",
            description=f"> **{member.name} ย้ายจาก {before.channel.name} ไปยัง {after.channel.name}**",
            color=nextcord.Color.yellow()
        )
        embed.set_thumbnail(url=member.avatar.url)
        await log_channel.send(embed=embed)



###[#[##[#[#[##[#[#[#[##[#[#








class VerificationModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(title="แบบฟอร์มแนะนำตัว")

        # TextInput สำหรับกรอกชื่อเล่น
        self.nickname = nextcord.ui.TextInput(
            label="ชื่อเล่น",
            placeholder="กรอกชื่อเล่นของคุณ",
            style=TextInputStyle.short,
            required=True
        )
        self.add_item(self.nickname)

        # TextInput สำหรับกรอกอายุ
        self.age = nextcord.ui.TextInput(
            label="อายุ",
            placeholder="กรอกอายุของคุณ",
            style=TextInputStyle.short,
            required=True
        )
        self.add_item(self.age)

        # TextInput สำหรับกรอกเพศ
        self.gender = nextcord.ui.TextInput(
            label="เพศ",
            placeholder="กรอกเพศของคุณ",
            style=TextInputStyle.short,
            required=True
        )
        self.add_item(self.gender)
        
       

        # TextInput สำหรับกรอก Link Facebook
        self.favorite_animal = nextcord.ui.TextInput(
            label="Link Facebook",
            placeholder="กรอก Link Facebook",
            style=TextInputStyle.short,
            required=True
        )
        self.add_item(self.favorite_animal)
        
        
         # TextInput ID Discord
        self.favorite = nextcord.ui.TextInput(
            label="ID Discord",
            placeholder="กรอก ID discord ของตัวเอง",
            style=TextInputStyle.short,
            required=True
        )
        self.add_item(self.favorite)
        
        

    async def callback(self, interaction: Interaction):
        # เพิ่มบทบาทให้กับผู้ใช้
        role = interaction.guild.get_role(ROLE_ID)
        if role:
            await interaction.user.add_roles(role)

        # สร้างข้อความ Embed สำหรับห้อง log
        log_embed = Embed(title="> ข้อมูลสมาชิก", color=nextcord.Color.green())
        log_embed.set_author(name=str(interaction.user), icon_url=interaction.user.avatar.url)
        log_embed.add_field(name="**ชื่อเล่น**", value=self.nickname.value, inline=False)
        log_embed.add_field(name="**อายุ**", value=self.age.value, inline=False)
        log_embed.add_field(name="**เพศ**", value=self.gender.value, inline=False)
       
        log_embed.add_field(name="**Link Facebook**", value=self.favorite_animal.value, inline=False)
        log_embed.add_field(name="**ID Discord**", value=self.favorite.value, inline=False)

        # ส่ง Embed ไปที่ช่อง log
        log_channel = interaction.guild.get_channel(log_vfy)
        if log_channel:
            await log_channel.send(embed=log_embed)

        # แจ้งให้ผู้ใช้ทราบว่าได้เพิ่มบทบาทเรียบร้อยแล้ว
        await interaction.response.send_message("> ยืนยันตัวตนสำเร็จ คุณได้รับบทบาทเรียบร้อยแล้ว ✅", ephemeral=True)

class VerifyButton(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="แนะนำตัว", emoji="<:scarfacemessage:1293494716880388096>", style=nextcord.ButtonStyle.secondary, custom_id="verify_button")
    async def verify_button_callback(self, button: nextcord.ui.Button, interaction: Interaction):
        # เปิด Modal ให้ผู้ใช้กรอกข้อมูล
        await interaction.response.send_modal(VerificationModal())

@bot.command()
async def setupvfy(ctx):
    
    embed0 = Embed(description=
    "```อ่านกฏให้เรียบร้อยก่อนดำเนินการกรอกข้อมูล                                  กรอกข้อมูลให้ถูกต้องครบถ้วน                          มิเช่นนั้นทางเราไม่สามารถยืนยันข้อมูลให้คุณได้```")
    
     
    embed0.set_image(url="https://media.discordapp.net/attachments/1374192317107273808/1374201374606098525/Arcane_Domain__icon.png?ex=682d3043&is=682bdec3&hm=17d94301af24f77703d2c459ce06dee07e94666a16c4a93b665abf5d7bd7721f&=&format=webp&quality=lossless")

    
    await ctx.send(embed=embed0 , view=VerifyButton())



















#####[#[#[#[#[#[#]]]]]]]]]]]]]]]]]
#####[#[#[#[##[#[#[#[##[#[#[##[#




quotes = [
    # แนวรัก
    "ความรักคือการเดินทางไปพร้อมกัน แม้บางครั้งจะต้องหยุดพักบ้าง แต่ขอเพียงเดินไปด้วยกันจนสุดทาง",
    "คนเราจะรักใครไม่ต้องมีเหตุผล เพราะความรักไม่ต้องการอะไรที่สมบูรณ์แบบ",
    "บางครั้งการอยู่ใกล้คนที่เรารัก ก็เป็นการรักษาใจตัวเองที่ดีที่สุด",
    
    # แนวเศร้า
    "บางครั้งการเงียบคือการรักษาตัวเองที่ดีที่สุด",
    "ความสุขที่ผ่านไป มักทิ้งรอยยิ้มและน้ำตาไว้เสมอ",
    "คิดถึงคือสิ่งที่ทำร้าย แต่ก็เป็นสิ่งที่ทำให้รู้ว่าเรายังมีหัวใจ",
    
    # แนวกวนๆ
    "ไม่มีใครสมบูรณ์แบบ ยกเว้นคนที่ทำอาหารเก่ง และไม่มีที่ติ",
    "ความรักก็เหมือนข้าวสวย ถ้าปล่อยไว้ในหม้อ เดี๋ยวมันก็แห้งและเหม็น",
    "แฟนไม่ต้องมี แต่รหัส Wi-Fi ต้องมี!",
    
    # แนวตลก
    "เคยอกหักหลายครั้ง จนบางครั้งก็อยากขอค่าแรงจากหัวใจตัวเอง",
    "คนที่เข้ามาในชีวิต มักมาเพื่อชวนกิน ไม่ใช่เพื่อมาเป็นแฟน",
    "ถ้าเธอไม่รักเรา เราจะรักตัวเองให้ดีกว่า",
    
    # แนวเครียด
    "ความเครียดทำให้เราเป็นผู้ใหญ่ แต่ก็ทำให้เราเป็นเด็กลงด้วย",
    "บางครั้งการเดินทางไปให้ไกล ก็ยังไม่พ้นจากปัญหาเดิม",
    "ถ้าทุกอย่างมันง่าย คนคงมีความสุขเต็มไปหมดแล้ว",
    
    # แนวเหนื่อย
    "บางครั้งการหยุดพักก็ไม่ใช่ความพ่ายแพ้ แต่เป็นการพักเพื่อสู้ต่อ",
    "เหนื่อยแค่ไหนก็ต้องไปต่อ เพราะไม่มีทางย้อนกลับ",
    "ถ้าเหนื่อยก็พัก อย่าฝืน จงให้ร่างกายได้พักเพื่อพลังที่ดีขึ้น"
]

@bot.command(name="คำคม")
async def คำคม(ctx):
    # สุ่มคำคมจากลิสต์
    quote = random.choice(quotes)

    # สร้าง Embed เพื่อตอบกลับ
    embed = nextcord.Embed(title="> **คำคมสำหรับคุณ**", description=quote)
    embed.set_footer(text="คำคมจากบอท")

    await ctx.send(embed=embed)













#]#]#]#]##]#]#]##]#]#]#]#]#]#  
        
##########################
fortunes = [
   
   
]

@bot.command(name="ดูดวง")
async def horoscope(ctx):
    fortune = random.choice(fortunes)
    
    # สร้าง Embed สำหรับผลการดูดวง
    embed = nextcord.Embed(title="> 🔮 บ้านของคุณคือ ", description=fortune, color=nextcord.Color.purple())
    embed.set_footer(text="ดูดวงโดยบอทสุดแม่น")
    
    # ส่ง Embed กลับไปในช่องแชท
    await ctx.send(embed=embed)
    
    
   

@bot.command()
async def setupplay(ctx):
    embed = nextcord.Embed(
        description="> **เมนูแจ้งเรื้อน**",
        color=nextcord.Color.red()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1373195010362572811/1373200756055998565/IMG_8146.jpg?ex=68298c5d&is=68283add&hm=669fcd9725e3a2aa442ff0fc7c2f4001e7b7e492acb05cf1c0291ddcf15c4f19&")
    embed.set_footer(text="กดปุ่ม รายงาน เพื่อแจ่งเรื้อน")


    view = AdminView()
    await ctx.send(embed=embed, view=view)

# ปุ่ม 3 ปุ่มในหน้า Admin
class AdminView(View):
    def __init__(self):
        super().__init__(timeout=None)  # ทำให้ปุ่มใช้งานได้ตลอด

    # ปุ่มแจ้งเรื้อน
    @ui.button(label="รายงาน", emoji="<a:1027052378706411543:1295109491313868840>", style=ButtonStyle.danger, custom_id="report_button")
    async def report_button_callback(self, button: Button, interaction: Interaction):
        await interaction.response.send_modal(ReportModal())

    # ปุ่มลงโทษ
    @ui.button(label="ลงโทษ", emoji="<a:2788demonshit:1210559553801035776>", style=ButtonStyle.danger, custom_id="punish_button")
    async def punish_button_callback(self, button: Button, interaction: Interaction):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("> **คุณไม่ใช่แอดมินกั้บ**", ephemeral=True)
        else:
            await interaction.response.send_modal(PunishModal())

    # ปุ่มเรียกตัว
    @ui.button(label="ประกาศตามตัว", emoji="<:icon_shop1:1258260296330379368>", style=ButtonStyle.secondary, custom_id="summon_button")
    async def summon_button_callback(self, button: Button, interaction: Interaction):
        await interaction.response.send_modal(SummonModal())

# Modal แจ้งเรื้อน
class ReportModal(Modal):
    def __init__(self):
        super().__init__(
            title="แจ้งเรื้อน",
            custom_id="report_modal"
        )
        self.add_item(TextInput(label="ข้อความ", placeholder="รายละเอียด", custom_id="report_message"))
        self.add_item(TextInput(label="ID ผู้ใช้", placeholder="ID ผู้ใช้", custom_id="user_id"))

    async def callback(self, interaction: Interaction):
        report_message = self.children[0].value
        user_id = self.children[1].value
        channel = get(interaction.guild.text_channels, name=log_kick)  # ช่องที่กำหนด

        embed = nextcord.Embed(title="> **รายงานการแจ้งเรื้อน จากสมาชิก**", color=nextcord.Color.red())
        embed.add_field(name="**ข้อความ**", value=report_message, inline=False)
        embed.add_field(name="**ID ผู้ใช้**", value=user_id, inline=False)

        await channel.send(embed=embed)
        await interaction.response.send_message("ดำเนินการรายงานเรียบร้อยแล้ว", ephemeral=True)

# Modal ลงโทษ
class PunishModal(Modal):
    def __init__(self):
        super().__init__(
            title="ลงโทษ",
            custom_id="punish_modal"
        )
        self.add_item(TextInput(label="ข้อหา", placeholder="รายละเอียดข้อหา", custom_id="punish_reason"))
        self.add_item(TextInput(label="ID ผู้ใช้", placeholder="ID ผู้ใช้", custom_id="user_id"))

    async def callback(self, interaction: Interaction):
        reason = self.children[0].value
        user_id = self.children[1].value

        try:
            member = await interaction.guild.fetch_member(int(user_id))
            await member.timeout(datetime.timedelta(days=3), reason=reason)  # หมดเวลา 1 วัน
            await interaction.response.send_message(f"ผู้ใช้ {member.display_name} ถูกลงโทษเป็นเวลา 3 วัน ไม่สามารถส่งข้อความและเข้าห้องเสียงได้ทุกกรณี", ephemeral=True)
        except:
            await interaction.response.send_message("ไม่พบผู้ใช้นี้", ephemeral=True)

# Modal เรียกตัว
class SummonModal(Modal):
    def __init__(self):
        super().__init__(
            title="ประกาศตามตัว",
            custom_id="summon_modal"
        )
        self.add_item(TextInput(label="ข้อความ", placeholder="ประกาศตามตัว", custom_id="summon_message"))
        self.add_item(TextInput(label="ID ผู้ใช้", placeholder="ID ผู้ใช้", custom_id="user_id"))

    async def callback(self, interaction: Interaction):
        summon_message = self.children[0].value
        user_id = self.children[1].value

        try:
            member = await interaction.guild.fetch_member(int(user_id))
            await member.send(f"> **คุณได้รับโดนหมายเรียกตามตัว กรุณาติดต่อทีมงานโดยด่วนภายใน 24 ชั่วโมง : {summon_message}**")
            await interaction.response.send_message("> **ประกาศตามตีวสำเร็จแล้ว**", ephemeral=True)
        except:
            await interaction.response.send_message("> ไม่สามารถส่ง DM ไปยังผู้ใช้นี้", ephemeral=True)



#############################

sweet_messages = [
"```Solmara☀️  กวางทองแสงเมตตา  ,   เป็นผู้นำ  , รุ่งโรจน์```",
   "```Ignivar🔥  นกฟีนิกซ์ไฟกล้าหาญ  ,   แรงบันดาลใจ  ,   หัวร้อน```",
"```Aqualis🌊  นากวารีน้ำใจเย็น  ,   ลึกซึ้ง  ,   มีสติปัญญา```",
 "```Ignivar🔥  นกฟีนิกซ์ไฟกล้าหาญ  ,   แรงบันดาลใจ  ,   หัวร้อน```",
"```Zephyros🌬  สิงห์ปีกลมลมเป็นอิสระ  ,   แปลกใหม่  ,   ช่างฝัน```",
"```Nocturnis🌑  งูเงาความมืดลึกลับ  ,  ช่างสังเกต  ,   เจ้าเล่ห์```",
"```Zephyros🌬  สิงห์ปีกลมลมเป็นอิสระ  ,   แปลกใหม่  ,   ช่างฝัน```",
"```Solmara☀️  กวางทองแสงเมตตา  ,   เป็นผู้นำ  , รุ่งโรจน์```"
]


@bot.event
async def on_message(message):
    
    if message.channel.id == phocute and message.attachments:
        
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(ext) for ext in ["png", "jpg", "jpeg", "gif"]):
                # สุ่มคำหวาน
                sweet_message = random.choice(sweet_messages)
                
                
                embed = nextcord.Embed(
                    title="> **✨ คำตอบจากบอท**",
                    description=sweet_message,
                    color=nextcord.Color.magenta()
                )
                embed.set_footer(text="**โปรดแจ้งแอดมินเพื่อรับยศบ้านตัวเอง**")
                
                
                await message.reply(embed=embed)
                break  

    await bot.process_commands(message)


#######]#]#]##]#]#]#]#]#]#]#]#]#]#

@bot.event
async def on_invite_create(invite):
    # ตรวจสอบว่าเซิร์ฟเวอร์มีช่อง Log ที่ถูกกำหนดไว้
    log_channel = bot.get_channel(log_invite)
    if log_channel is None:
        print("ไม่พบช่อง log กรุณาตรวจสอบว่า log_invite ถูกตั้งค่าอย่างถูกต้อง")
        return

    # สร้าง Embed สำหรับแจ้งเตือนการสร้างลิงก์เชิญ
    embed = nextcord.Embed(
        title="> 📨 : มีการสร้างลิงก์เชิญใหม่",
        color=0x3151F7
    )
    embed.add_field(name="**🔗 : ลิงก์เชิญ**", value=invite.url, inline=False)
    embed.add_field(name="**👤 : สร้างโดย**", value=invite.inviter.mention, inline=True)
    embed.add_field(name="**จำนวนครั้งที่ใช้ได้**", value=invite.max_uses or "ไม่จำกัด", inline=True)
    embed.add_field(name="**หมดอายุใน**", value=f"{invite.max_age // 60} นาที" if invite.max_age else "ไม่หมดอายุ", inline=True)
    embed.set_footer(text="การแจ้งเตือนการสร้างลิงก์เชิญ")

    # ส่ง Embed ไปยังช่อง log ที่กำหนด
    await log_channel.send(embed=embed)

        
##############################




#############################





############%%%###################


# รายชื่อภูมิภาคและจังหวัดทั้งหมด
regions = {
    "ภาคกลาง": ["กรุงเทพมหานคร", "นนทบุรี", "ปทุมธานี", "พระนครศรีอยุธยา", "ลพบุรี", "สมุทรปราการ", "นครปฐม", "สมุทรสาคร", "อ่างทอง"],
    "ภาคตะวันออกเฉียงเหนือ": ["ขอนแก่น", "นครราชสีมา", "อุดรธานี", "บุรีรัมย์", "สุรินทร์", "สกลนคร", "มหาสารคาม", "ศรีสะเกษ", "ร้อยเอ็ด"],
    "ภาคเหนือ": ["เชียงใหม่", "เชียงราย", "ลำปาง", "ลำพูน", "แพร่", "น่าน", "พะเยา", "แม่ฮ่องสอน", "อุตรดิตถ์"],
    "ภาคตะวันออก": ["ชลบุรี", "ระยอง", "จันทบุรี", "ตราด", "ปราจีนบุรี", "สระแก้ว", "ฉะเชิงเทรา"],
    "ภาคใต้": ["สุราษฎร์ธานี", "นครศรีธรรมราช", "สงขลา", "ปัตตานี", "ยะลา", "พัทลุง", "นราธิวาส", "ตรัง", "ภูเก็ต", "กระบี่"],
    "ภาคตะวันตก": ["กาญจนบุรี", "ราชบุรี", "เพชรบุรี", "ประจวบคีรีขันธ์", "ตาก"],
    "ภาคเหนือบน": ["น่าน", "พะเยา", "เชียงใหม่", "เชียงราย", "แม่ฮ่องสอน"],
    "ภาคกลางตอนล่าง": ["นครปฐม", "ราชบุรี", "สมุทรสงคราม", "เพชรบุรี", "นครราชสีมา", "บุรีรัมย์", "สุรินทร์", "ศรีสะเกษ"],
    
}

# คำสั่งนี้สามารถใช้ได้แค่แอดมินเท่านั้น
@bot.command(name="setup77")
@commands.has_permissions(administrator=True)
async def setup77(ctx):
    #เมนูเลือกภูมิภาค
    class RegionSelect(Select):
        def __init__(self):
            options = [SelectOption(label=f"🌍 {region}", value=region) for region in regions.keys()]
            super().__init__(placeholder="เลือกภูมิภาค", min_values=1, max_values=1, options=options)

        async def callback(self, interaction: Interaction):
            selected_region = self.values[0]
            provinces = regions[selected_region]
            province_view = View()
            province_view.add_item(ProvinceSelect(provinces))
            await interaction.response.send_message(
                embed=nextcord.Embed(
                    title="> เลือกจังหวัด", 
                    description="> **เลือกจังหวัดจากภาคที่เลือก**", 
                    color=nextcord.Color.blue()
                ),
                view=province_view, ephemeral=True
            )
    
    # เมนูเลือกจังหวัด
    class ProvinceSelect(Select):
        def __init__(self, provinces):
            options = [SelectOption(label=province, value=province) for province in provinces]
            super().__init__(placeholder="เลือกจังหวัด", min_values=1, max_values=1, options=options)

        async def callback(self, interaction: Interaction):
            selected_province = self.values[0]
            role = nextcord.utils.get(interaction.guild.roles, name=selected_province)
            if role:
                await interaction.user.add_roles(role)
                await interaction.response.send_message(f"> ** คุณได้รับบทบาท {role.name} เรียบร้อยแล้วกั้บบบ**", ephemeral=True)
                #ค้นหาช่อง log ที่กำหนดไว้
                log_channel = nextcord.utils.get(interaction.guild.channels, name=log_77)
                if log_channel:
                    # สร้าง Embed สำหรับ log
                    log_embed = nextcord.Embed(
                        title="> **มีการรับบทบาท77จังหวัด**",
                        description=f">>> ผู้ใช้ {interaction.user.mention} \nได้รับบทบาท: **{role.name}**",
                        color=nextcord.Color.green()
                    )
                    log_embed.set_thumbnail(url=interaction.user.avatar.url if interaction.user.avatar else interaction.user.default_avatar.url)
                    log_embed.set_footer(text=f"ID ผู้ใช้: {interaction.user.id}")
                    
                    # ส่ง Embed log ไปยังช่อง log
                    await log_channel.send(embed=log_embed)
    
    # สร้างและส่ง Embed สำหรับการเลือกภูมิภาค
    region_view = View()
    region_view.add_item(RegionSelect())
    
    embed = nextcord.Embed(
        title="> ตั้งค่าข้อมูล", 
        description="> **กรุณาเลือกภูมิภาคเพื่อดูจังหวัด**", 
        color=nextcord.Color.blue()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1297382088009580555/1297549805597364264/IMG_0660.jpg?ex=671654ec&is=6715036c&hm=965b216efe1184456be2c751a00e8e36c934422b84201027f9fb10e288aa7dbf&")
    
    
    await ctx.send(embed=embed, view=region_view)
    
##[#[##[##[[#[#[#[##[#[#]]]]]]]]]]



class Send(nextcord.ui.View):
    def __init__(self, user: str, user2: str):
        self.user = user
        self.user2 = user2
        super().__init__(timeout=None)
    
    @nextcord.ui.button(label='ส่งการแจ้งเตือน', style=nextcord.ButtonStyle.primary, custom_id='senddm')
    async def senddm(self, button, interaction: nextcord.Interaction):
        button.disabled = True
        button.label = 'ส่งแล้ว'
        member = interaction.guild.get_member(int(self.user))
        data = json.load(open(f'./database/data_profile/{member}.json', 'r', encoding='utf-8'))
        age = str(data['age'])
        sex = str(data['sex'])
        province = str(data['province'])
        unique = str(data['unique'])
        member2 = interaction.guild.get_member(int(self.user2))
        embed = nextcord.Embed(
            color=0x42f5e6
        )
        embed.add_field(name='อายุ', value=f'{age}', inline=True)
        embed.add_field(name='เพศ', value=f'{sex}', inline=True)
        embed.add_field(name='จังหวัด', value=f'{province}', inline=True)
        embed.add_field(name='นิสัย', value=f'{unique}', inline=False)
        embed.set_thumbnail(member.avatar)
        thailand_timezone = pytz.timezone('Asia/Bangkok')
        success_time = datetime.datetime.now(thailand_timezone)
        embed.timestamp = success_time
        await member2.send(content=f'> ผู้ใช้ {member.mention} ได้สะกิดคุณ!', embed=embed)
        return await interaction.response.edit_message(view=self)
    
    @nextcord.ui.button(label='สุ่มใหม่', style=nextcord.ButtonStyle.red, custom_id='rerandom')
    async def rerandom(self, button, interaction: nextcord.Interaction):
        try:
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        except FileNotFoundError:
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'province': '',
                    'unique': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)

            embed = nextcord.Embed(description='> คุณยังไม่ได้ตั้งค่าข้อมูล', color=0xff0000)
            return await interaction.edit.send_message(embed=embed, view=None)

        data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        sex = str(data['sex'])
        age = str(data['age'])
        province = str(data['province'])
        unique = str(data['unique'])
        if sex == '' or age == '' or province == '' or unique == '':
            embed = nextcord.Embed(description='> โปรดตั้งค่าข้อมูลให้ครบถ้วน', color=0xff0000)
            return await interaction.response.edit_message(embed=embed, view=None)
        else:
            while True:
                pathDatabase = './database/data_profile'
                db = os.listdir(pathDatabase)
                result = random.choice(db)
                if 'search' in result:
                    continue
                matchAuth = json.load(open(f'{pathDatabase}/{result}', 'r', encoding='utf-8'))
                userid = int(matchAuth['userid'])
                sex2 = str(matchAuth['sex'])
                age2 = str(matchAuth['age'])
                province2 = str(matchAuth['province'])
                unique2 = str(matchAuth['unique'])
                if sex2 == '' or age2 == '' or province2 == '' or unique2 == '':
                    continue
                else:
                    if str(matchAuth['userid']) == str(interaction.user.id):
                        continue
                    else:
                        member = interaction.guild.get_member(int(matchAuth['userid']))
                        embed = nextcord.Embed(color=0x00f2ff)
                        embed.add_field(name='อายุ', value=f'{age2} ปี', inline=True)
                        embed.add_field(name='เพศ', value=f'{sex2}', inline=True)
                        embed.add_field(name='จังหวัด', value=f'{province2}', inline=True)
                        embed.add_field(name='นิสัย', value=f'{unique2}', inline=False)
                        embed.set_thumbnail(member.avatar)
                        return await interaction.response.edit_message(content=f'คุณต้องการจับคู่กับ {member.mention} ใช่หรือไม่?', embed=embed, view=Send(str(interaction.user.id), str(matchAuth['userid'])))

class Send2(nextcord.ui.View):
    def __init__(self, user: str, user2: str):
        self.user = user
        self.user2 = user2
        super().__init__(timeout=None)
    
    @nextcord.ui.button(label='ส่งการแจ้งเตือน', style=nextcord.ButtonStyle.primary, custom_id='senddmbobo')
    async def senddmbobo(self, button, interaction: nextcord.Interaction):
        button.disabled = True
        button.label = 'ส่งแล้ว'
        member = interaction.guild.get_member(int(self.user))
        data = json.load(open(f'./database/data_profile/{member}.json', 'r', encoding='utf-8'))
        age = str(data['age'])
        sex = str(data['sex'])
        province = str(data['province'])
        unique = str(data['unique'])
        member2 = interaction.guild.get_member(int(self.user2))
        embed = nextcord.Embed(
            color=0x42f5e6
        )
        embed.add_field(name='อายุ', value=f'{age}', inline=True)
        embed.add_field(name='เพศ', value=f'{sex}', inline=True)
        embed.add_field(name='จังหวัด', value=f'{province}', inline=True)
        embed.add_field(name='นิสัย', value=f'{unique}', inline=False)
        embed.set_thumbnail(member.avatar)
        thailand_timezone = pytz.timezone('Asia/Bangkok')
        success_time = datetime.datetime.now(thailand_timezone)
        embed.timestamp = success_time
        await member2.send(content=f'ผู้ใช้ {member.mention} ได้สะกิดคุณ!', embed=embed)
        return await interaction.response.edit_message(view=self)
    
    @nextcord.ui.button(label='สุ่มใหม่', style=nextcord.ButtonStyle.red, custom_id='rerandombobo')
    async def rerandombobo(self, button, interaction: nextcord.Interaction):
        data2 = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
        sex = str(data2['sex'])
        age = str(data2['age'])
        age2 = str(data2['age2'])
        province = str(data2['province'])
        if sex == '' or age == '' or age2 == '' or province == '':
            while True:
                pathDatabase = './database/data_profile'
                db = os.listdir(pathDatabase)
                result = random.choice(db)
                if 'search' in result:
                    continue
                print(f'{pathDatabase}/{result}')
                optz = json.load(open(f'{pathDatabase}/{result}', 'r', encoding='utf-8'))
                userid = int(optz['userid'])
                sex2 = str(optz['sex'])
                age2 = str(optz['age'])
                province2 = str(optz['province'])
                unique = str(optz['unique'])
                if sex2 == '' or age2 == '' or province2 == '' or unique == '':
                    continue
                else:
                    if str(optz['userid']) == str(interaction.user.id):
                        continue
                    else:
                        member = interaction.guild.get_member(int(optz['userid']))
                        embed = nextcord.Embed(color=0x00f2ff)
                        embed.add_field(name='อายุ', value=f'{age2} ปี', inline=True)
                        embed.add_field(name='เพศ', value=f'{sex2}', inline=True)
                        embed.add_field(name='จังหวัด', value=f'{province2}', inline=True)
                        embed.add_field(name='นิสัย', value=f'{unique}', inline=False)
                        embed.set_thumbnail(member.avatar)
                        return await interaction.response.edit_message(content=f'คุณต้องการจับคู่กับ {member.mention} ใช่หรือไม่?', embed=embed, view=Send(str(interaction.user.id), str(optz['userid'])))
        else:
            fetch_error = 0
            while True:
                if fetch_error == 20:
                    fetch_error = 0
                    embed = nextcord.Embed(description='> ไม่พบผู้ใช้ตามตัวกรองดังกล่าว!', color=0xff0000)
                    return await interaction.response.edit_message(embed=embed, view=None)
                pathDatabase = './database/data_profile'
                db = os.listdir(pathDatabase)
                result = random.choice(db)
                if 'search' in result:
                    continue
                print(f'{pathDatabase}/{result}')
                optz = json.load(open(f'{pathDatabase}/{result}', 'r', encoding='utf-8'))
                userid = int(optz['userid'])
                sex2 = str(optz['sex'])
                age12 = str(optz['age'])
                province2 = str(optz['province'])
                unique = str(optz['unique'])
                if sex2 == '' or age == '' or province2 == '' or unique == '':
                    continue
                else:
                    if str(optz['userid']) == str(interaction.user.id):
                        continue
                    else:
                        if int(str(age12)) >= int(str(age)) and int(str(age12)) <= int(str(age2)):
                            if str(sex) == 'ชาย':
                                if str(sex2) == 'ชาย':
                                    if str(province2) == str(province):
                                        member = interaction.guild.get_member(int(optz['userid']))
                                        embed = nextcord.Embed(color=0x00f2ff)
                                        embed.add_field(name='อายุ', value=f'{age12} ปี', inline=True)
                                        embed.add_field(name='เพศ', value=f'{sex2}', inline=True)
                                        embed.add_field(name='จังหวัด', value=f'{province2}', inline=True)
                                        embed.add_field(name='นิสัย', value=f'{unique}', inline=False)
                                        embed.set_thumbnail(member.avatar)
                                        return await interaction.response.edit_message(content=f'คุณต้องการจับคู่กับ {member.mention} ใช่หรือไม่?', embed=embed, view=Send2(str(interaction.user.id), str(optz['userid'])))
                                    else:
                                        fetch_error += 1
                                        continue
                                else:
                                    fetch_error += 1
                                    continue
                            if str(sex) == 'หญิง':
                                if str(sex2) == 'หญิง':
                                    if str(province2) == str(province):
                                        member = interaction.guild.get_member(int(optz['userid']))
                                        embed = nextcord.Embed(color=0x00f2ff)
                                        embed.add_field(name='อายุ', value=f'{age12} ปี', inline=True)
                                        embed.add_field(name='เพศ', value=f'{sex2}', inline=True)
                                        embed.add_field(name='จังหวัด', value=f'{province2}', inline=True)
                                        embed.add_field(name='นิสัย', value=f'{unique}', inline=False)
                                        embed.set_thumbnail(member.avatar)
                                        return await interaction.response.edit_message(content=f'คุณต้องการจับคู่กับ {member.mention} ใช่หรือไม่?', embed=embed, view=Send2(str(interaction.user.id), str(optz['userid'])))
                                    else:
                                        fetch_error += 1
                                        continue
                        else:
                            fetch_error += 1
                            continue


class SetAge(nextcord.ui.Modal):
    def __init__(self):
        super().__init__('การตั้งค่าอายุ')
        self.age = nextcord.ui.TextInput(label='กรุณาระบุอายุของคุณ', max_length=2, required=True)
        self.add_item(self.age)
    
    async def callback(self, interaction: nextcord.Interaction):
        data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        userid = str(data['userid'])
        sex = str(data['sex'])
        age = str(data['age'])
        province = str(data['province'])
        unique = str(data['unique'])

        try:
            ageInput = int(self.age.value)
        except ValueError:
            embed = nextcord.Embed(description='> กรุณาระบุอายุให้ถูกต้อง', color=0xff0000)
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        
        if int(ageInput) > 50:
            embed = nextcord.Embed(description='> กรุณาระบุอายุให้ถูกต้อง', color=0xff0000)
            return await interaction.response.send_message(embed=embed, ephemeral=True)

        with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as update:
            action_new = {
                'userid': str(userid),
                'sex': str(sex),
                'age': str(self.age.value),
                'province': str(province),
                'unique': str(unique)
            }
            json.dump(action_new, update, indent=4, ensure_ascii=False)
        
        embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อย',color=0x4efc03)
        return await interaction.response.send_message(embed=embed, ephemeral=True, delete_after=1)

class SetAge2(nextcord.ui.Modal):
    def __init__(self):
        super().__init__('การตั้งค่าอายุ')
        self.age = nextcord.ui.TextInput(label='อายุต่ำสุด', max_length=2, required=True)
        self.add_item(self.age)
        self.age2 = nextcord.ui.TextInput(label='อายุสูงสุด', max_length=2, required=True)
        self.add_item(self.age2)
    
    async def callback(self, interaction: nextcord.Interaction):
        data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
        userid = str(data['userid'])
        sex = str(data['sex'])
        age = str(data['age'])
        province = str(data['province'])

        try:
            ageInput = int(self.age.value)
            ageInput2 = int(self.age2.value)
        except ValueError:
            embed = nextcord.Embed(description='> กรุณาระบุอายุให้ถูกต้อง', color=0xff0000)
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        
        if int(ageInput) < 1 or int(ageInput2) > 50:
            embed = nextcord.Embed(description='> กรุณาระบุอายุให้ถูกต้อง', color=0xff0000)
            return await interaction.response.send_message(embed=embed, ephemeral=True)

        with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as update:
            action_new = {
                'userid': str(userid),
                'sex': str(sex),
                'age': str(self.age.value),
                'age2': str(self.age2.value),
                'province': str(province)
            }
            json.dump(action_new, update, indent=4, ensure_ascii=False)
        
        embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อย',color=0x4efc03)
        return await interaction.response.send_message(embed=embed, ephemeral=True, delete_after=1)

class SetUnique(nextcord.ui.Modal):
    def __init__(self):
        super().__init__('การตั้งค่านิสัย')
        self.unique = nextcord.ui.TextInput(label='กรุณาระบุนิสัยของคุณ', required=True, style=nextcord.TextInputStyle.paragraph)
        self.add_item(self.unique)
    
    async def callback(self, interaction: nextcord.Interaction):
        data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        userid = str(data['userid'])
        sex = str(data['sex'])
        age = str(data['age'])
        province = str(data['province'])
        unique = str(data['unique'])
        
        with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as update:
            action_new = {
                'userid': str(userid),
                'sex': str(sex),
                'age': str(age),
                'province': str(province),
                'unique': str(self.unique.value)
            }
            json.dump(action_new, update, indent=4, ensure_ascii=False)
        
        embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อย',color=0x4efc03)
        return await interaction.response.send_message(embed=embed, ephemeral=True, delete_after=1)


class SelectSexAuth(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='ชาย',
                description='คลิกที่นี่เพื่อเลือก เพศชาย',
                value='1'
            ),
            nextcord.SelectOption(
                label='หญิง',
                description='คลิกที่นี่เพื่อเลือก เพศหญิง',
                value='2'
            )
        ]
        super().__init__(placeholder='โปรดเลือกเพศของคุณ!', options=options, custom_id='selected-sex')
    async def callback(self, interaction: nextcord.Interaction):
        data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        userid = str(data['userid'])
        sex = str(data['sex'])
        age = str(data['age'])
        province = str(data['province'])
        unique = str(data['unique'])
        
        if self.values[0] == '1':
            sex = 'ชาย'
        if self.values[0] == '2':
            sex = 'หญิง'
        
        with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as update:
            action_new = {
                'userid': str(userid),
                'sex': str(sex),
                'age': str(age),
                'province': str(province),
                'unique': str(unique)
            }
            json.dump(action_new, update, indent=4, ensure_ascii=False)
        
        embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อย',color=0x4efc03)
        return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)

class SelectSexAuth2(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='ชาย',
                description='คลิกที่นี่เพื่อเลือก เพศชาย',
                value='1'
            ),
            nextcord.SelectOption(
                label='หญิง',
                description='คลิกที่นี่เพื่อเลือก เพศหญิง',
                value='2'
            )
        ]
        super().__init__(placeholder='โปรดเลือกเพศของคุณ!', options=options, custom_id='selected-sex')
    async def callback(self, interaction: nextcord.Interaction):
        data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
        userid = str(data['userid'])
        sex = str(data['sex'])
        age = str(data['age'])
        age2 = str(data['age2'])
        province = str(data['province'])
        
        if self.values[0] == '1':
            sex = 'ชาย'
        if self.values[0] == '2':
            sex = 'หญิง'
        
        with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as update:
            action_new = {
                'userid': str(userid),
                'sex': str(sex),
                'age': str(age),
                'age2': str(age2),
                'province': str(province)
            }
            json.dump(action_new, update, indent=4, ensure_ascii=False)
        
        embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อย',color=0x4efc03)
        return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)



class North(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='เชียงใหม่',
                description='คลิกที่นี่เพื่อเลือกจังหวัด เชียงใหม่',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='ลำพูน',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ลำพูน',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='ลำปาง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ลำปาง',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='อุตรดิตถ์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อุตรดิตถ์',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='แพร่',
                description='คลิกที่นี่เพื่อเลือกจังหวัด แพร่',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='น่าน',
                description='คลิกที่นี่เพื่อเลือกจังหวัด น่าน',
                emoji='🌍',
                value='6',
            ),
            nextcord.SelectOption(
                label='พะเยา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พะเยา',
                emoji='🌍',
                value='7',
            ),
            nextcord.SelectOption(
                label='เชียงราย',
                description='คลิกที่นี่เพื่อเลือกจังหวัด เชียงราย',
                emoji='🌍',
                value='8',
            ),
            nextcord.SelectOption(
                label='แม่ฮ่องสอน',
                description='คลิกที่นี่เพื่อเลือกจังหวัด แม่ฮ่องสอน',
                emoji='🌍',
                value='9',
            ),
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'เชียงใหม่',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ลำพูน',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ลำปาง',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'อุตรดิตถ์',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'แพร่',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '6':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'น่าน',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '7':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'พะเยา',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '8':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'เชียงราย',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '9':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'แม่ฮ่องสอน',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)

class North2(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='เชียงใหม่',
                description='คลิกที่นี่เพื่อเลือกจังหวัด เชียงใหม่',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='ลำพูน',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ลำพูน',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='ลำปาง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ลำปาง',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='อุตรดิตถ์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อุตรดิตถ์',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='แพร่',
                description='คลิกที่นี่เพื่อเลือกจังหวัด แพร่',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='น่าน',
                description='คลิกที่นี่เพื่อเลือกจังหวัด น่าน',
                emoji='🌍',
                value='6',
            ),
            nextcord.SelectOption(
                label='พะเยา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พะเยา',
                emoji='🌍',
                value='7',
            ),
            nextcord.SelectOption(
                label='เชียงราย',
                description='คลิกที่นี่เพื่อเลือกจังหวัด เชียงราย',
                emoji='🌍',
                value='8',
            ),
            nextcord.SelectOption(
                label='แม่ฮ่องสอน',
                description='คลิกที่นี่เพื่อเลือกจังหวัด แม่ฮ่องสอน',
                emoji='🌍',
                value='9',
            ),
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'เชียงใหม่'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ลำพูน'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ลำปาง'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'อุตรดิตถ์'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'แพร่'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '6':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'น่าน'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '7':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'พะเยา'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '8':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'เชียงราย'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '9':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'แม่ฮ่องสอน'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)


class Central(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='กรุงเทพมหานคร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด กรุงเทพมหานคร',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='สมุทปราการ',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สมุทปราการ',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='นนทบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นนทบุรี',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='ปทุมธานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ปทุมธานี',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='พระนครศรีอยุธยา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พระนครศรีอยุธยา',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='อ่างทอง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อ่างทอง',
                emoji='🌍',
                value='6',
            ),
            nextcord.SelectOption(
                label='ลพบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ลพบุรี',
                emoji='🌍',
                value='7',
            ),
            nextcord.SelectOption(
                label='สิงห์บุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สิงห์บุรี',
                emoji='🌍',
                value='8',
            ),
            nextcord.SelectOption(
                label='ชัยนาท',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ชัยนาท',
                emoji='🌍',
                value='9',
            ),
            nextcord.SelectOption(
                label='สระบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สระบุรี',
                emoji='🌍',
                value='10',
            ),
            nextcord.SelectOption(
                label='นครนายก',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครนายก',
                emoji='🌍',
                value='11',
            ),
            nextcord.SelectOption(
                label='นครสวรรค์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครสวรรค์',
                emoji='🌍',
                value='12',
            ),
            nextcord.SelectOption(
                label='อุทัยธานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อุทัยธานี',
                emoji='🌍',
                value='13',
            ),
            nextcord.SelectOption(
                label='กำแพงเพชร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด กำแพงเพชร',
                emoji='🌍',
                value='14',
            ),
            nextcord.SelectOption(
                label='สุขโขทัย',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สุขโขทัย',
                emoji='🌍',
                value='15',
            ),
            nextcord.SelectOption(
                label='พิษณุโลก',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พิษณุโลก',
                emoji='🌍',
                value='16',
            ),
            nextcord.SelectOption(
                label='พิจิตร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พิจิตร',
                emoji='🌍',
                value='17',
            ),
            nextcord.SelectOption(
                label='เพชรบูรณ์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด เพชรบูรณ์',
                emoji='🌍',
                value='18',
            ),
            nextcord.SelectOption(
                label='สุพรรณบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สุพรรณบุรี',
                emoji='🌍',
                value='19',
            ),
            nextcord.SelectOption(
                label='นครปฐม',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครปฐม',
                emoji='🌍',
                value='20',
            ),
            nextcord.SelectOption(
                label='สมุทรสาคร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สมุทรสาคร',
                emoji='🌍',
                value='21',
            ),
            nextcord.SelectOption(
                label='สมุทรสงคราม',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สมุทรสงคราม',
                emoji='🌍',
                value='22',
            ),
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'กรุงเทพมหานคร',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สมุทรปราการ',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'นนทบุรี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ปทุมธานี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'พระนครศรีอยุธยา',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '6':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'อ่างทอง',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '7':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ลพบุรี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '8':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สิงห์บุรี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '9':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ชัยนาท',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '10':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สระบุรี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '11':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'นครนายก',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '12':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'นครสวรรค์',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '13':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'อุทัยธานี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '14':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'กำแพงเพชร',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '15':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สุขโขทัย',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '16':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'พิษณุโลก',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '17':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'พิจิตร',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '18':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'เพชรบูรณ์',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '19':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สุพรรณบุรี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '20':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'นครปฐม',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '21':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สมุทรสาคร',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '22':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สมุทรสงคราม',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)

class Central2(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='กรุงเทพมหานคร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด กรุงเทพมหานคร',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='สมุทปราการ',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สมุทปราการ',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='นนทบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นนทบุรี',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='ปทุมธานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ปทุมธานี',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='พระนครศรีอยุธยา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พระนครศรีอยุธยา',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='อ่างทอง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อ่างทอง',
                emoji='🌍',
                value='6',
            ),
            nextcord.SelectOption(
                label='ลพบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ลพบุรี',
                emoji='🌍',
                value='7',
            ),
            nextcord.SelectOption(
                label='สิงห์บุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สิงห์บุรี',
                emoji='🌍',
                value='8',
            ),
            nextcord.SelectOption(
                label='ชัยนาท',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ชัยนาท',
                emoji='🌍',
                value='9',
            ),
            nextcord.SelectOption(
                label='สระบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สระบุรี',
                emoji='🌍',
                value='10',
            ),
            nextcord.SelectOption(
                label='นครนายก',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครนายก',
                emoji='🌍',
                value='11',
            ),
            nextcord.SelectOption(
                label='นครสวรรค์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครสวรรค์',
                emoji='🌍',
                value='12',
            ),
            nextcord.SelectOption(
                label='อุทัยธานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อุทัยธานี',
                emoji='🌍',
                value='13',
            ),
            nextcord.SelectOption(
                label='กำแพงเพชร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด กำแพงเพชร',
                emoji='🌍',
                value='14',
            ),
            nextcord.SelectOption(
                label='สุขโขทัย',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สุขโขทัย',
                emoji='🌍',
                value='15',
            ),
            nextcord.SelectOption(
                label='พิษณุโลก',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พิษณุโลก',
                emoji='🌍',
                value='16',
            ),
            nextcord.SelectOption(
                label='พิจิตร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พิจิตร',
                emoji='🌍',
                value='17',
            ),
            nextcord.SelectOption(
                label='เพชรบูรณ์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด เพชรบูรณ์',
                emoji='🌍',
                value='18',
            ),
            nextcord.SelectOption(
                label='สุพรรณบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สุพรรณบุรี',
                emoji='🌍',
                value='19',
            ),
            nextcord.SelectOption(
                label='นครปฐม',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครปฐม',
                emoji='🌍',
                value='20',
            ),
            nextcord.SelectOption(
                label='สมุทรสาคร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สมุทรสาคร',
                emoji='🌍',
                value='21',
            ),
            nextcord.SelectOption(
                label='สมุทรสงคราม',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สมุทรสงคราม',
                emoji='🌍',
                value='22',
            ),
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'กรุงเทพมหานคร'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สมุทรปราการ'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'นนทบุรี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ปทุมธานี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'พระนครศรีอยุธยา'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '6':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'อ่างทอง'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '7':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ลพบุรี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '8':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สิงห์บุรี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '9':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ชัยนาท'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '10':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สระบุรี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '11':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'นครนายก'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '12':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'นครสวรรค์'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '13':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'อุทัยธานี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '14':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'กำแพงเพชร'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '15':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สุโขทัย'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '16':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'พิษณุโลก'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '17':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'พิจิตร'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '18':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'เพชรบูรณ์'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '19':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สุพรรณบุรี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '20':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'นครปฐม'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '21':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สมุทรสาคร'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '22':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สมุทรสงคราม'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)

class Esan(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='นครราชสีมา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครราชสีมา',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='บุรีรัมย์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด บุรีรัมย์',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='สุรินทร์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สุรินทร์',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='ศรีสะเกษ',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ศรีสะเกษ',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='อุบลราชธานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อุบลราชธานี',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='ยโสธร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ยโสธร',
                emoji='🌍',
                value='6',
            ),
            nextcord.SelectOption(
                label='ชัยภูมิ',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ชัยภูมิ',
                emoji='🌍',
                value='7',
            ),
            nextcord.SelectOption(
                label='อำนาจเจริญ',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อำนาจเจริญ',
                emoji='🌍',
                value='8',
            ),
            nextcord.SelectOption(
                label='หนองบัวลำภู',
                description='คลิกที่นี่เพื่อเลือกจังหวัด หนองบัวลำภู',
                emoji='🌍',
                value='9',
            ),
            nextcord.SelectOption(
                label='ขอนแก่น',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ขอนแก่น',
                emoji='🌍',
                value='10',
            ),
            nextcord.SelectOption(
                label='อุดรธานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อุดรธานี',
                emoji='🌍',
                value='11',
            ),
            nextcord.SelectOption(
                label='เลย',
                description='คลิกที่นี่เพื่อเลือกจังหวัด เลย',
                emoji='🌍',
                value='12',
            ),
            nextcord.SelectOption(
                label='หนองคาย',
                description='คลิกที่นี่เพื่อเลือกจังหวัด หนองคาย',
                emoji='🌍',
                value='13',
            ),
            nextcord.SelectOption(
                label='มหาสารคาม',
                description='คลิกที่นี่เพื่อเลือกจังหวัด มหาสารคาม',
                emoji='🌍',
                value='14',
            ),
            nextcord.SelectOption(
                label='ร้อยเอ็ด',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ร้อยเอ็ด',
                emoji='🌍',
                value='15',
            ),
            nextcord.SelectOption(
                label='กาฬสินธุ์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด กาฬสินธุ์',
                emoji='🌍',
                value='16',
            ),
            nextcord.SelectOption(
                label='สกลนคร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สกลนคร',
                emoji='🌍',
                value='17',
            ),
            nextcord.SelectOption(
                label='นครพนม',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครพนม',
                emoji='🌍',
                value='18',
            ),
            nextcord.SelectOption(
                label='มุกดาหาร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด มุกดาหาร',
                emoji='🌍',
                value='19',
            ),
            nextcord.SelectOption(
                label='บึงกาฬ',
                description='คลิกที่นี่เพื่อเลือกจังหวัด บึงกาฬ',
                emoji='🌍',
                value='20',
            )
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'นครราชสีมา',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'บุรีรัมย์',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สุรินทร์',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ศรีสะเกษ',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'อุบลราชธานี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '6':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ยโสธร',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '7':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ชัยภูมิ',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '8':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'อำนาจเจริญ',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '9':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'หนองบัวลำภู',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '10':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ขอนแก่น',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '11':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'อุดรธานี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '12':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'เลย',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '13':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'หนองคาย',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '14':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'มหาสารคาม',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '15':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ร้อยเอ็ด',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '16':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'กาฬสินธุ์',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '17':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สกลนคร',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '18':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'นครพนม',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '19':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'มุกดาหาร',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '20':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'บึงกาฬ',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)

class Esan2(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='นครราชสีมา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครราชสีมา',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='บุรีรัมย์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด บุรีรัมย์',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='สุรินทร์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สุรินทร์',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='ศรีสะเกษ',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ศรีสะเกษ',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='อุบลราชธานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อุบลราชธานี',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='ยโสธร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ยโสธร',
                emoji='🌍',
                value='6',
            ),
            nextcord.SelectOption(
                label='ชัยภูมิ',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ชัยภูมิ',
                emoji='🌍',
                value='7',
            ),
            nextcord.SelectOption(
                label='อำนาจเจริญ',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อำนาจเจริญ',
                emoji='🌍',
                value='8',
            ),
            nextcord.SelectOption(
                label='หนองบัวลำภู',
                description='คลิกที่นี่เพื่อเลือกจังหวัด หนองบัวลำภู',
                emoji='🌍',
                value='9',
            ),
            nextcord.SelectOption(
                label='ขอนแก่น',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ขอนแก่น',
                emoji='🌍',
                value='10',
            ),
            nextcord.SelectOption(
                label='อุดรธานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด อุดรธานี',
                emoji='🌍',
                value='11',
            ),
            nextcord.SelectOption(
                label='เลย',
                description='คลิกที่นี่เพื่อเลือกจังหวัด เลย',
                emoji='🌍',
                value='12',
            ),
            nextcord.SelectOption(
                label='หนองคาย',
                description='คลิกที่นี่เพื่อเลือกจังหวัด หนองคาย',
                emoji='🌍',
                value='13',
            ),
            nextcord.SelectOption(
                label='มหาสารคาม',
                description='คลิกที่นี่เพื่อเลือกจังหวัด มหาสารคาม',
                emoji='🌍',
                value='14',
            ),
            nextcord.SelectOption(
                label='ร้อยเอ็ด',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ร้อยเอ็ด',
                emoji='🌍',
                value='15',
            ),
            nextcord.SelectOption(
                label='กาฬสินธุ์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด กาฬสินธุ์',
                emoji='🌍',
                value='16',
            ),
            nextcord.SelectOption(
                label='สกลนคร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สกลนคร',
                emoji='🌍',
                value='17',
            ),
            nextcord.SelectOption(
                label='นครพนม',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครพนม',
                emoji='🌍',
                value='18',
            ),
            nextcord.SelectOption(
                label='มุกดาหาร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด มุกดาหาร',
                emoji='🌍',
                value='19',
            ),
            nextcord.SelectOption(
                label='บึงกาฬ',
                description='คลิกที่นี่เพื่อเลือกจังหวัด บึงกาฬ',
                emoji='🌍',
                value='20',
            )
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'นครราชสีมา'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'บุรีรัมย์'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สุรินทร์'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ศรีสะเกษ'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'อุบลราชธานี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '6':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ยโสธร'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '7':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ชัยภูมิ'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '8':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'อำนาจเจริญ'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '9':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'หนองบัวลำภู'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '10':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ขอนแก่น'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '11':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'อุดรธานี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '12':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'เลย'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '13':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'หนองคาย'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '14':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'มหาสารคาม'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '15':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ร้อยเอ็ด'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '16':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'กาฬสินธุ์'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '17':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สกลนคร'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '18':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'นครพนม'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '19':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'มุกดาหาร'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '20':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'บึงกาฬ'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)

class Western(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='ตาก',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ตาก',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='ราชบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ราชบุรี',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='กาญจนบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด กาญจนบุรี',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='เพชรบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด เพชรบุรี',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='ประจวบคีรีขันธ์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ประจวบคีรีขันธ์',
                emoji='🌍',
                value='5',
            ),
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ตาก',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ราชบุรี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'กาญจนบุรี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'เพชรบุรี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ประจวบคีรีขันธ์',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)

class Western2(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='ตาก',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ตาก',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='ราชบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ราชบุรี',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='กาญจนบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด กาญจนบุรี',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='เพชรบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด เพชรบุรี',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='ประจวบคีรีขันธ์',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ประจวบคีรีขันธ์',
                emoji='🌍',
                value='5',
            ),
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ตาก'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ราชบุรี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'กาญจนบุรี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'เพชรบุรี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ประจวบคีรีขันธ์'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)


class Eastern(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='ชลบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ชลบุรี',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='ระยอง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ระยอง',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='จันทบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด จันทบุรี',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='ตราด',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ตราด',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='ฉะเชิงเทรา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ฉะเชิงเทรา',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='ปราจีนบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ปราจีนบุรี',
                emoji='🌍',
                value='6',
            ),
            nextcord.SelectOption(
                label='สระแก้ว',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สระแก้ว',
                emoji='🌍',
                value='7',
            ),
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ชลบุรี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ระยอง',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'จันทบุรี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ตราด',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ฉะเชิงเทรา',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '6':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ปราจีนบุรี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '7':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สระแก้ว',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)

class Eastern2(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='ชลบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ชลบุรี',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='ระยอง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ระยอง',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='จันทบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด จันทบุรี',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='ตราด',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ตราด',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='ฉะเชิงเทรา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ฉะเชิงเทรา',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='ปราจีนบุรี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ปราจีนบุรี',
                emoji='🌍',
                value='6',
            ),
            nextcord.SelectOption(
                label='สระแก้ว',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สระแก้ว',
                emoji='🌍',
                value='7',
            ),
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ชลบุรี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ระยอง'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'จันทบุรี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ตราด'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ฉะเชิงเทรา'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '6':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ปราจีนบุรี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '7':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สระแก้ว'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)



class South(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='นครศรีธรรมราช',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครศรีธรรมราช',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='กระบี่',
                description='คลิกที่นี่เพื่อเลือกจังหวัด กระบี่',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='พังงา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พังงา',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='ภูเก็ต',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ภูเก็ต',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='สุราษฏร์ธานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สุราษฏร์ธานี',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='ระนอง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ระนอง',
                emoji='🌍',
                value='6',
            ),
            nextcord.SelectOption(
                label='ชุมพร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ชุมพร',
                emoji='🌍',
                value='7',
            ),
            nextcord.SelectOption(
                label='สงขลา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สงขลา',
                emoji='🌍',
                value='8',
            ),
            nextcord.SelectOption(
                label='สตูล',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สตูล',
                emoji='🌍',
                value='9',
            ),
            nextcord.SelectOption(
                label='ตรัง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ตรัง',
                emoji='🌍',
                value='10',
            ),
            nextcord.SelectOption(
                label='พัทลุง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พัทลุง',
                emoji='🌍',
                value='11',
            ),
            nextcord.SelectOption(
                label='ปัตตานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ปัตตานี',
                emoji='🌍',
                value='12',
            ),
            nextcord.SelectOption(
                label='ยะลา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ยะลา',
                emoji='🌍',
                value='13',
            ),
            nextcord.SelectOption(
                label='นราธิวาส',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นราธิวาส',
                emoji='🌍',
                value='14',
            ),
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'นครศรีธรรมราช',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'กระบี่',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'พังงา',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ภูเก็ต',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สุราษฏร์ธานี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '6':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ระนอง',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '7':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ชุมพร',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '8':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สงขลา',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '9':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'สตูล',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '10':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ตรัง',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '11':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'พัทลุง',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '12':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ปัตตานี',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '13':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'ยะลา',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '14':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'province': 'นราธิวาส',
                    'unique': str(data['unique'])
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)

class South2(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='นครศรีธรรมราช',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นครศรีธรรมราช',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='กระบี่',
                description='คลิกที่นี่เพื่อเลือกจังหวัด กระบี่',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='พังงา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พังงา',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='ภูเก็ต',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ภูเก็ต',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='สุราษฏร์ธานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สุราษฏร์ธานี',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='ระนอง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ระนอง',
                emoji='🌍',
                value='6',
            ),
            nextcord.SelectOption(
                label='ชุมพร',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ชุมพร',
                emoji='🌍',
                value='7',
            ),
            nextcord.SelectOption(
                label='สงขลา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สงขลา',
                emoji='🌍',
                value='8',
            ),
            nextcord.SelectOption(
                label='สตูล',
                description='คลิกที่นี่เพื่อเลือกจังหวัด สตูล',
                emoji='🌍',
                value='9',
            ),
            nextcord.SelectOption(
                label='ตรัง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ตรัง',
                emoji='🌍',
                value='10',
            ),
            nextcord.SelectOption(
                label='พัทลุง',
                description='คลิกที่นี่เพื่อเลือกจังหวัด พัทลุง',
                emoji='🌍',
                value='11',
            ),
            nextcord.SelectOption(
                label='ปัตตานี',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ปัตตานี',
                emoji='🌍',
                value='12',
            ),
            nextcord.SelectOption(
                label='ยะลา',
                description='คลิกที่นี่เพื่อเลือกจังหวัด ยะลา',
                emoji='🌍',
                value='13',
            ),
            nextcord.SelectOption(
                label='นราธิวาส',
                description='คลิกที่นี่เพื่อเลือกจังหวัด นราธิวาส',
                emoji='🌍',
                value='14',
            ),
        ]
        super().__init__(placeholder='โปรดเลือกจังหวัดที่คุณอยู่', options=options, custom_id='selected-contryzone')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        zonelist = ['เชียงใหม่','นครราชสีมา','กาญจนบุรี','ตาก','อุบลราชธานี','สุราษฎร์ธานี','ชัยภูมิ','แม่ฮ่องสอน',
        'เพชรบูรณ์','ลำปาง','อุดรธานี','เชียงราย','น่าน','เลย','ขอนแก่น','พิษณุโลก','บุรีรัมย์','นครศรีธรรมราช',
        'สกลนคร','นครสวรรค์','ศรีสะเกษ','กำแพงเพชร','ร้อยเอ็ด','สุรินทร์','อุตรดิตถ์','สงขลา','สระแก้ว',
        'กาฬสินธุ์','อุทัยธานี','สุโขทัย','แพร่','ประจวบคีรีขันธ์','จันทบุรี','พะเยา','เพชรบุรี','ลพบุรี','ชุมพร',
        'นครพนม','สุพรรณบุรี','ฉะเชิงเทรา','มหาสารคาม','ราชบุรี','ตรัง','ปราจีนบุรี','กระบี่','พิจิตร',
        'ยะลา','ลำพูน','นราธิวาส','ชลบุรี','มุกดาหาร','บึงกาฬ','พังงา','ยโสธร','หนองบัวลำภู','สระบุรี',
        'ระยอง','พัทลุง','ระนอง','อำนาจเจริญ','หนองคาย','ตราด','พระนครศรีอยุธยา','สตูล','ชัยนาท','นครปฐม',
        'นครนายก','ปัตตานี','กรุงเทพมหานคร','ปทุมธานี','สมุทรปราการ','อ่างทอง','สมุทรสาคร','สิงห์บุรี','นนทบุรี',
        'ภูเก็ต','สมุทรสงคราม']
        if self.values[0] == '1':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'นครศรีธรรมราช'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '2':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'กระบี่'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '3':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'พังงา'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '4':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ภูเก็ต'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '5':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สุราษฏร์ธานี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '6':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ระนอง'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '7':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ชุมพร'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '8':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สงขลา'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '9':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'สตูล'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '10':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ตรัง'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '11':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'พัทลุง'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '12':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ปัตตานี'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '13':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'ยะลา'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)
        if self.values[0] == '14':
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as userNew:
                atk = {
                    'userid': str(interaction.user.id),
                    'sex': str(data['sex']),
                    'age': str(data['age']),
                    'age2': str(data['age2']),
                    'province': 'นราธิวาส'
                }
                json.dump(atk, userNew, indent=4, ensure_ascii=False)
            embed = nextcord.Embed(title='✅ อัพเดทข้อมูลเรียบร้อยแล้ว!',color=0xa2ff00)
            return await interaction.response.edit_message(embed=embed, view=None, delete_after=1)




class V1(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(North())

class V2(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Central())

class V3(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Esan())

class V4(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Western())

class V5(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Eastern())

class V6(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(South())

class V11(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(North2())

class V22(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Central2())

class V33(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Esan2())

class V44(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Western2())

class V55(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Eastern2())

class V66(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(South2())

class SelectContry1(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='ภาคเหนือ',
                description='คลิกที่นี่เพื่อเลือก ภาคเหนือ',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='ภาคกลาง',
                description='คลิกที่นี่เพื่อเลือก ภาคกลาง',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='ภาคอีสาน',
                description='คลิกที่นี่เพื่อเลือก ภาคอีสาน',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='ภาคตะวันตก',
                description='คลิกที่นี่เพื่อเลือก ภาคตะวันตก',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='ภาคตะวันออก',
                description='คลิกที่นี่เพื่อเลือก ภาคตะวันออก',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='ภาคใต้',
                description='คลิกที่นี่เพื่อเลือก ภาคใต้',
                emoji='🌍',
                value='6',
            ),
        ]
        super().__init__(placeholder='โปรด - เลือกภาคของคุณ', options=options, custom_id='selected-contry')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        if self.values[0] == '1':
            return await interaction.response.edit_message(view=V1())
        if self.values[0] == '2':
            return await interaction.response.edit_message(view=V2())
        if self.values[0] == '3':
            return await interaction.response.edit_message(view=V3())
        if self.values[0] == '4':
            return await interaction.response.edit_message(view=V4())
        if self.values[0] == '5':
            return await interaction.response.edit_message(view=V5())
        if self.values[0] == '6':
            return await interaction.response.edit_message(view=V6())

class SelectContry2(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(
                label='ภาคเหนือ',
                description='คลิกที่นี่เพื่อเลือก ภาคเหนือ',
                emoji='🌍',
                value='1',
            ),
            nextcord.SelectOption(
                label='ภาคกลาง',
                description='คลิกที่นี่เพื่อเลือก ภาคกลาง',
                emoji='🌍',
                value='2',
            ),
            nextcord.SelectOption(
                label='ภาคอีสาน',
                description='คลิกที่นี่เพื่อเลือก ภาคอีสาน',
                emoji='🌍',
                value='3',
            ),
            nextcord.SelectOption(
                label='ภาคตะวันตก',
                description='คลิกที่นี่เพื่อเลือก ภาคตะวันตก',
                emoji='🌍',
                value='4',
            ),
            nextcord.SelectOption(
                label='ภาคตะวันออก',
                description='คลิกที่นี่เพื่อเลือก ภาคตะวันออก',
                emoji='🌍',
                value='5',
            ),
            nextcord.SelectOption(
                label='ภาคใต้',
                description='คลิกที่นี่เพื่อเลือก ภาคใต้',
                emoji='🌍',
                value='6',
            ),
        ]
        super().__init__(placeholder='โปรด - เลือกภาคของคุณ', options=options, custom_id='selected-contry')
        # embed = nextcord.Embed(color=0x00f7ff)
    
    async def callback(self, interaction: nextcord.Interaction):
        if self.values[0] == '1':
            return await interaction.response.edit_message(view=V11())
        if self.values[0] == '2':
            return await interaction.response.edit_message(view=V22())
        if self.values[0] == '3':
            return await interaction.response.edit_message(view=V33())
        if self.values[0] == '4':
            return await interaction.response.edit_message(view=V44())
        if self.values[0] == '5':
            return await interaction.response.edit_message(view=V55())
        if self.values[0] == '6':
            return await interaction.response.edit_message(view=V66())
    
class ViewProvince(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectContry1())

class ViewProvince2(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectContry2())

class SelectSex(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectSexAuth())

class SelectSex2(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(SelectSexAuth2())

class ProfileSetting(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(label='เลือกเพศ', style=nextcord.ButtonStyle.primary, custom_id='sexselection')
    async def sexselection(self, button, interaction: nextcord.Interaction):
        return await interaction.response.send_message(view=SelectSex(), ephemeral=True)

    
    @nextcord.ui.button(label='อายุ', style=nextcord.ButtonStyle.green, custom_id='ageselection')
    async def ageselection(self, button, interaction: nextcord.Interaction):
        return await interaction.response.send_modal(SetAge())
    
    @nextcord.ui.button(label='จังหวัด', style=nextcord.ButtonStyle.red, custom_id='provinceselection')
    async def provinceselection(self, button, interaction: nextcord.Interaction):
        return await interaction.response.send_message(view=ViewProvince(), ephemeral=True)
    
    @nextcord.ui.button(label='นิสัย', style=nextcord.ButtonStyle.primary, custom_id='uniqueselection')
    async def uniqueselection(self, button, interaction: nextcord.Interaction):
        return await interaction.response.send_modal(SetUnique())
    
    @nextcord.ui.button(label='รีโหลดข้อมูล', row=1, style=nextcord.ButtonStyle.primary, custom_id='reloadselection')
    async def reloadselection(self, button, interaction: nextcord.Interaction):
        try:
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        except FileNotFoundError:
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'province': '',
                    'unique': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)
        except json.decoder.JSONDecodeError:
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'province': '',
                    'unique': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)

        data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        sex = str(data['sex'])
        age = str(data['age'])
        province = str(data['province'])
        unique = str(data['unique'])
        if sex == '':
            sex = 'ยังไม่ได้ตั้งค่า'
        if age == '':
            age = 'ยังไม่ได้ตั้งค่า'
        if province == '':
            province = 'ยังไม่ได้ตั้งค่า'
        if unique == '':
            unique = 'ยังไม่ได้ตั้งค่า'
        embed = nextcord.Embed(
            title='การตั้งค่าข้อมูลส่วนตัว',
            description=f'เพศ : {sex}\nอายุ : {age}\nจังหวัด : {province}\nนิสัย : {unique}',
            color=0x4efc03
        )
        embed.set_thumbnail(interaction.user.avatar)
        return await interaction.response.edit_message(embed=embed, view=ProfileSetting())
    
    @nextcord.ui.button(label='รีเซ็ตข้อมูล', row=1, style=nextcord.ButtonStyle.red, custom_id='resetselection')
    async def resetselection(self, button, interaction: nextcord.Interaction):
        try:
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        except FileNotFoundError:
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': str(interaction.user.id),
                    'sex': '',
                    'age': '',
                    'province': '',
                    'unique': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)
        except json.decoder.JSONDecodeError:
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'province': '',
                    'unique': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)
            
            embed = nextcord.Embed(title='✅ อัพเดทช้อมูลเรียบร้อยแล้ว', color=0x4efc03)
            return await interaction.response.send_message(embed=embed, ephemeral=True, delete_after=1)
        
        with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as newuser:
            action = {
                'userid': str(interaction.user.id),
                'sex': '',
                'age': '',
                'province': '',
                'unique': ''
            }
            json.dump(action, newuser, indent=4, ensure_ascii=False)
        
        data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        sex = str(data['sex'])
        age = str(data['age'])
        province = str(data['province'])
        unique = str(data['unique'])
        if sex == '':
            sex = 'ยังไม่ได้ตั้งค่า'
        if age == '':
            age = 'ยังไม่ได้ตั้งค่า'
        if province == '':
            province = 'ยังไม่ได้ตั้งค่า'
        if unique == '':
            unique = 'ยังไม่ได้ตั้งค่า'
        embed = nextcord.Embed(
            title='การตั้งค่าข้อมูลส่วนตัว',
            description=f'เพศ : {sex}\nอายุ : {age}\nจังหวัด : {province}\nนิสัย : {unique}',
            color=0x4efc03
        )
        embed.set_thumbnail(interaction.user.avatar)
        return await interaction.response.edit_message(embed=embed)

class ProfileSetting2(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(label='เลือกเพศ', style=nextcord.ButtonStyle.primary, custom_id='zasexselection')
    async def zasexselection(self, button, interaction: nextcord.Interaction):
        return await interaction.response.send_message(view=SelectSex2(), ephemeral=True)

    
    @nextcord.ui.button(label='อายุ', style=nextcord.ButtonStyle.green, custom_id='zaageselection')
    async def zaageselection(self, button, interaction: nextcord.Interaction):
        return await interaction.response.send_modal(SetAge2())
    
    @nextcord.ui.button(label='จังหวัด', style=nextcord.ButtonStyle.red, custom_id='zaprovinceselection')
    async def zaprovinceselection(self, button, interaction: nextcord.Interaction):
        return await interaction.response.send_message(view=ViewProvince2(), ephemeral=True)
    
    @nextcord.ui.button(label='รีโหลดข้อมูล', row=1, style=nextcord.ButtonStyle.primary, custom_id='zareloadselection')
    async def zareloadselection(self, button, interaction: nextcord.Interaction):
        try:
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
        except FileNotFoundError:
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'age2': '',
                    'province': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)
        except json.decoder.JSONDecodeError:
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'age2': '',
                    'province': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)

        data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
        sex = str(data['sex'])
        age = str(data['age'])
        age2 = str(data['age2'])
        province = str(data['province'])
        if sex == '':
            sex = 'ยังไม่ได้ตั้งค่า'
        if age == '' or age2 == '':
            age = 'ยังไม่ได้ตั้งค่า'
            age2 = 'ยังไม่ได้ตั้งค่า'
        if province == '':
            province = 'ยังไม่ได้ตั้งค่า'
        
        embed = nextcord.Embed(
            title='ตั้งค่าการค้นหา',
            description=f'เพศ : {sex}\nอายุ : {age} - {age2}\nจังหวัด : {province}',
            color=0x4efc03
        )
        return await interaction.response.edit_message(embed=embed)
        
    
    @nextcord.ui.button(label='รีเซ็ตข้อมูล', row=1, style=nextcord.ButtonStyle.red, custom_id='zaresetselection')
    async def zaresetselection(self, button, interaction: nextcord.Interaction):
        try:
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
        except FileNotFoundError:
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': str(interaction.user.id),
                    'sex': '',
                    'age': '',
                    'age2': '',
                    'province': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)
        except json.decoder.JSONDecodeError:
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'age2': '',
                    'province': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)
            
            embed = nextcord.Embed(title='✅ อัพเดทช้อมูลเรียบร้อยแล้ว', color=0x4efc03)
            return await interaction.response.send_message(embed=embed, ephemeral=True, delete_after=1)
        
        with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as newuser:
            action = {
                'userid': str(interaction.user.id),
                'sex': '',
                'age': '',
                'age2': '',
                'province': ''
            }
            json.dump(action, newuser, indent=4, ensure_ascii=False)
        
        data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
        sex = str(data['sex'])
        age = str(data['age'])
        age2 = str(data['age2'])
        province = str(data['province'])
        if sex == '':
            sex = 'ยังไม่ได้ตั้งค่า'
        if age == '' or age2 == '':
            age = 'ยังไม่ได้ตั้งค่า'
            age2 = 'ยังไม่ได้ตั้งค่า'
        if province == '':
            province = 'ยังไม่ได้ตั้งค่า'
        embed = nextcord.Embed(
            title='ตั้งค่าการค้นหา',
            description=f'เพศ : {sex}\nอายุ : {age} - {age2}\nจังหวัด : {province}',
            color=0x4efc03
        )
        return await interaction.response.edit_message(embed=embed)


class Button(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(label='ตั้งค่าข้อมูลส่วนตัว', style=nextcord.ButtonStyle.primary, custom_id='profile')
    async def profile(self, button, interaction: nextcord.Interaction):
        print(f'{interaction.user.name}')
        try:
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        except FileNotFoundError:
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'province': '',
                    'unique': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)
        except json.decoder.JSONDecodeError:
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'province': '',
                    'unique': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)

        data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        sex = str(data['sex'])
        age = str(data['age'])
        province = str(data['province'])
        unique = str(data['unique'])
        if sex == '':
            sex = 'ยังไม่ได้ตั้งค่า'
        if age == '':
            age = 'ยังไม่ได้ตั้งค่า'
        if province == '':
            province = 'ยังไม่ได้ตั้งค่า'
        if unique == '':
            unique = 'ยังไม่ได้ตั้งค่า'
        embed = nextcord.Embed(
            title='การตั้งค่าข้อมูลส่วนตัว',
            description=f'เพศ : {sex}\nอายุ : {age}\nจังหวัด : {province}\nนิสัย : {unique}',
            color=0x4efc03
        )
        embed.set_thumbnail(interaction.user.avatar)
        return await interaction.response.send_message(embed=embed, ephemeral=True, view=ProfileSetting())
    
    
    @nextcord.ui.button(label='กรอกการค้นหา', style=nextcord.ButtonStyle.grey, custom_id='filter')
    async def filter(self, button, interaction: nextcord.Interaction):
        try:
            data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
        except FileNotFoundError:
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'age2': '',
                    'province': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)
        except json.decoder.JSONDecodeError:
            with open(f'./database/data_profile/{interaction.user.name}_search.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'age2': '',
                    'province': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)

        
        data = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
        userid = str(data['userid'])
        sex = str(data['sex'])
        age = str(data['age'])
        age2 = str(data['age2'])
        province = str(data['province'])
        if sex == '':
            sex = 'ยังไม่ได้ตั้งค่า'
        if age == '' or age2 == '':
            age = 'ยังไม่ได้ตั้งค่า'
            age2 = 'ยังไม่ได้ตั้งค่า'
        if province == '':
            province = 'ยังไม่ได้ตั้งค่า'
        embed = nextcord.Embed(
            title='ตั้งค่าการค้นหา',
            description=f'เพศ : {sex}\nอายุ : {age} - {age2}\nจังหวัด : {province}',
            color=0x4efc03
        )
        return await interaction.response.send_message(embed=embed, view=ProfileSetting2(), ephemeral=True)

    
    @nextcord.ui.button(label='แมทต์', style=nextcord.ButtonStyle.red, custom_id='match')
    async def match(self, button, interaction: nextcord.Interaction):
        try:
            data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        except FileNotFoundError:
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'province': '',
                    'unique': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)
        except json.decoder.JSONDecodeError:
            with open(f'./database/data_profile/{interaction.user.name}.json', 'w+', encoding='utf-8') as newuser:
                action = {
                    'userid': f'{interaction.user.id}',
                    'sex': '',
                    'age': '',
                    'province': '',
                    'unique': ''
                }
                json.dump(action, newuser, indent=4, ensure_ascii=False)

            embed = nextcord.Embed(description='> คุณยังไม่ได้ตั้งค่าข้อมูล', color=0xff0000)
            return await interaction.response.send_message(embed=embed, ephemeral=True)

        data = json.load(open(f'./database/data_profile/{interaction.user.name}.json', 'r', encoding='utf-8'))
        sex = str(data['sex'])
        age = str(data['age'])
        province = str(data['province'])
        unique = str(data['unique'])
        if sex == '' or age == '' or province == '' or unique == '':
            embed = nextcord.Embed(description='> โปรดตั้งค่าข้อมูลส่วนตัวก่อน!', color=0xff0000)
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            try:
                data2 = json.load(open(f'./database/data_profile/{interaction.user.name}_search.json', 'r', encoding='utf-8'))
                sex = str(data2['sex'])
                age = str(data2['age'])
                age2 = str(data2['age2'])
                province = str(data2['province'])
                if sex == '' or age == '' or age2 == '' or province == '':
                    while True:
                        pathDatabase = './database/data_profile'
                        db = os.listdir(pathDatabase)
                        result = random.choice(db)
                        if 'search' in result:
                            continue
                        print(f'{pathDatabase}/{result}')
                        optz = json.load(open(f'{pathDatabase}/{result}', 'r', encoding='utf-8'))
                        userid = int(optz['userid'])
                        sex2 = str(optz['sex'])
                        age2 = str(optz['age'])
                        province2 = str(optz['province'])
                        unique = str(optz['unique'])
                        if sex2 == '' or age2 == '' or province2 == '' or unique == '':
                            continue
                        else:
                            if str(optz['userid']) == str(interaction.user.id):
                                continue
                            else:
                                member = interaction.guild.get_member(int(optz['userid']))
                                embed = nextcord.Embed(color=0x00f2ff)
                                embed.add_field(name='อายุ', value=f'{age2} ปี', inline=True)
                                embed.add_field(name='เพศ', value=f'{sex2}', inline=True)
                                embed.add_field(name='จังหวัด', value=f'{province2}', inline=True)
                                embed.add_field(name='นิสัย', value=f'{unique}', inline=False)
                                embed.set_thumbnail(member.avatar)
                                return await interaction.response.send_message(content=f'คุณต้องการจับคู่กับ {member.mention} ใช่หรือไม่?', embed=embed, ephemeral=True, view=Send(str(interaction.user.id), str(optz['userid'])))
                else:
                    fetch_error = 0
                    while True:
                        if fetch_error == 20:
                            fetch_error = 0
                            embed = nextcord.Embed(description='> ไม่พบผู้ใช้ตามตัวกรองดังกล่าว!', color=0xff0000)
                            return await interaction.response.send_message(embed=embed, ephemeral=True)
                        pathDatabase = './database/data_profile'
                        db = os.listdir(pathDatabase)
                        result = random.choice(db)
                        if 'search' in result:
                            continue
                        print(f'{pathDatabase}/{result}')
                        optz = json.load(open(f'{pathDatabase}/{result}', 'r', encoding='utf-8'))
                        userid = int(optz['userid'])
                        sex2 = str(optz['sex'])
                        age12 = str(optz['age'])
                        province2 = str(optz['province'])
                        unique = str(optz['unique'])
                        if sex2 == '' or age == '' or province2 == '' or unique == '':
                            continue
                        else:
                            if str(optz['userid']) == str(interaction.user.id):
                                continue
                            else:
                                if int(str(age12)) >= int(str(age)) and int(str(age12)) <= int(str(age2)):
                                    if str(sex) == 'ชาย':
                                        if str(sex2) == 'ชาย':
                                            if str(province2) == str(province):
                                                member = interaction.guild.get_member(int(optz['userid']))
                                                embed = nextcord.Embed(color=0x00f2ff)
                                                embed.add_field(name='อายุ', value=f'{age12} ปี', inline=True)
                                                embed.add_field(name='เพศ', value=f'{sex2}', inline=True)
                                                embed.add_field(name='จังหวัด', value=f'{province2}', inline=True)
                                                embed.add_field(name='นิสัย', value=f'{unique}', inline=False)
                                                embed.set_thumbnail(member.avatar)
                                                return await interaction.response.send_message(content=f'คุณต้องการจับคู่กับ {member.mention} ใช่หรือไม่?', embed=embed, ephemeral=True, view=Send2(str(interaction.user.id), str(optz['userid'])))
                                            else:
                                                fetch_error += 1
                                                continue
                                        else:
                                            fetch_error += 1
                                            continue
                                    if str(sex) == 'หญิง':
                                        if str(sex2) == 'หญิง':
                                            if str(province2) == str(province):
                                                member = interaction.guild.get_member(int(optz['userid']))
                                                embed = nextcord.Embed(color=0x00f2ff)
                                                embed.add_field(name='อายุ', value=f'{age12} ปี', inline=True)
                                                embed.add_field(name='เพศ', value=f'{sex2}', inline=True)
                                                embed.add_field(name='จังหวัด', value=f'{province2}', inline=True)
                                                embed.add_field(name='นิสัย', value=f'{unique}', inline=False)
                                                embed.set_thumbnail(member.avatar)
                                                return await interaction.response.send_message(content=f'คุณต้องการจับคู่กับ {member.mention} ใช่หรือไม่?', embed=embed, ephemeral=True, view=Send2(str(interaction.user.id), str(optz['userid'])))
                                            else:
                                                fetch_error += 1
                                                continue
                                else:
                                    fetch_error += 1
                                    continue

                
            except FileNotFoundError:
                error = 0
                while True:
                    if error == 20:
                        embed = nextcord.Embed(description='> ไม่พบผู้ใช้!', color=0xff0000)
                        return await interaction.response.send_message(embed=embed, ephemeral=True)
                    pathDatabase = './database/data_profile'
                    db = os.listdir(pathDatabase)
                    result = random.choice(db)
                    if 'search' in result:
                        continue
                    matchAuth = json.load(open(f'{pathDatabase}/{result}', 'r', encoding='utf-8'))
                    userid = int(matchAuth['userid'])
                    sex2 = str(matchAuth['sex'])
                    age2 = str(matchAuth['age'])
                    province2 = str(matchAuth['province'])
                    unique2 = str(matchAuth['unique'])
                    if sex2 == '' or age2 == '' or province2 == '' or unique2 == '':
                        continue
                    else:
                        if str(matchAuth['userid']) == str(interaction.user.id):
                            error += 1
                            continue
                        else:
                            member = interaction.guild.get_member(int(matchAuth['userid']))
                            embed = nextcord.Embed(color=0x00f2ff)
                            embed.add_field(name='อายุ', value=f'{age2} ปี', inline=True)
                            embed.add_field(name='เพศ', value=f'{sex2}', inline=True)
                            embed.add_field(name='จังหวัด', value=f'{province2}', inline=True)
                            embed.add_field(name='นิสัย', value=f'{unique2}', inline=False)
                            embed.set_thumbnail(member.avatar)
                            return await interaction.response.send_message(content=f'คุณต้องการจับคู่กับ {member.mention} ใช่หรือไม่?', embed=embed, ephemeral=True, view=Send(str(interaction.user.id), str(matchAuth['userid'])))


@bot.event
async def on_connect():
    bot.add_view(Button())
    bot.add_view(ProfileSetting())

@bot.command(name="setuplove2")
async def setuplove2(ctx):
        embed = nextcord.Embed(
            color=nextcord.Color.blue())
        embed.set_image(url='https://cdn.discordapp.com/attachments/1210590999055962213/1212956900270936135/1.png?ex=65f3b924&is=65e14424&hm=0b1ab4ee901d42504588e8e0bab4b2a72d8664b9335c3dcf4471a542fe1efeb1&')
        await ctx.channel.send(embed=embed, view=Button())

bot.run(token)
