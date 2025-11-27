class script(object):
    START_TXT = """𝗛𝗶 𝗠𝗮𝘁𝗲,🥰 𝗡𝗶𝗰𝗲 𝗧𝗼 𝗠𝗲𝗲𝘁 𝗬𝗼𝘂 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>,
𝗜 𝗔𝗺 𝗔 𝗦𝗶𝗺𝗽𝗹𝗲 𝗔𝘂𝘁𝗼 𝗙𝗶𝗹𝘁𝗲𝗿 𝗕𝗼𝘁 🪄, 
𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂,🖥 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍
⚠️𝖬𝗈𝗋𝖾 𝖧𝖾𝗅𝗉 𝖧𝗂𝗍 /help
👑 𝗠𝘆 𝗖𝗿𝗲𝗮𝘁𝗼𝗿 @Leomc_bot"""

    STATUS_TXT = """📊 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    STATUS_TXT2 = """📂 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌     - <code>{}</code>

𒆜  𝗗𝗕 1️⃣
𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌         - <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾   - <code>{}</code>MB
𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾    - <code>{}</code>MB

𒆜 𝗗𝗕 2️⃣
𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌         - <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾   - <code>{}</code>MB
𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾    - <code>{}</code>MB


𒆜 𝗗𝗕 3️⃣ 
🕵️ 𝖴𝗌𝖾𝗋𝗌            - <code>{}</code>
🖥️ 𝖢𝗁𝖺𝗍𝗌            - <code>{}</code>
𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾   - <code>{}</code>MB
𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾    - <code>{}</code>MB"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    CUSTOM_FILE_CAPTION = """<b>{file_name}</b>\n\n🔘 size - {file_size}"""
