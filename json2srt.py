import json

def convert_timestamp_to_srt(timestamp_text):
    parts = timestamp_text.split(":")
    
    if len(parts) == 1:
        hours = 0
        minutes = 0
        seconds = int(parts[0])
    elif len(parts) == 2:
        hours = 0
        minutes = int(parts[0])
        seconds = int(parts[1])
    elif len(parts) == 3:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
    else:
        raise ValueError(f"Invalid time format: {timestamp_text}")
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    start_hours = total_seconds // 3600
    start_minutes = (total_seconds % 3600) // 60
    start_seconds = total_seconds % 60
    start_time = f"{start_hours:02d}:{start_minutes:02d}:{start_seconds:02d},000"
    
    total_seconds_end = total_seconds + 10
    end_hours = total_seconds_end // 3600
    end_minutes = (total_seconds_end % 3600) // 60
    end_seconds = total_seconds_end % 60
    end_time = f"{end_hours:02d}:{end_minutes:02d}:{end_seconds:02d},000"
    
    return start_time, end_time

def render_chat(chats):
    chat_rendered = []
    subtitle_index = 1
    
    for chat in chats:
        item = chat['replayChatItemAction']['actions'][0]
        if 'addChatItemAction' not in item:
            continue
        item = item['addChatItemAction']['item']
        
        if 'liveChatTextMessageRenderer' in item:
            chat_renderer = item['liveChatTextMessageRenderer']
            author = chat_renderer['authorName']['simpleText']
            message_runs = chat_renderer['message']['runs']
            timestamp_text = chat_renderer['timestampText']['simpleText']

            parsed_runs = []
            for run in message_runs:
                if 'text' in run:
                    parsed_runs.append(run['text'])
                elif 'emoji' in run:
                    parsed_runs.append(run['emoji']['shortcuts'][0])
            message = ' '.join(parsed_runs)
            
            start_time, end_time = convert_timestamp_to_srt(timestamp_text)
            
            srt_entry = f"{subtitle_index}\n{start_time} --> {end_time}\n{author}: {message}\n"
            chat_rendered.append(srt_entry)
            subtitle_index += 1
            
        elif 'liveChatViewerEngagementMessageRenderer' in item:
            pass
        else:
            pass
    return chat_rendered

if __name__ == "__main__":
    filename = "live_chat.json"

    chats = []
    with open(filename, encoding="utf-8") as infile:
        for line in infile.readlines():
            chats.append(json.loads(line))

    chat_rendered = render_chat(chats)
    
    with open("subtitle.srt", 'w', encoding="utf-8") as outfile:
        for chat in chat_rendered:
            print(chat, file=outfile)
