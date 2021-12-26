#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyrogram.types import Message


def extract_user(message: Message) -> (int, str):
    """extracts the user from a message"""
    user_id = None
    user_first_name = None

    if (
        message.reply_to_message
    ):
        if message.reply_to_message.from_user:
            user_id = message.reply_to_message.from_user.id
            user_first_name = message.reply_to_message.from_user.first_name

        elif message.reply_to_message.sender_chat:
            user_id = message.reply_to_message.sender_chat.id
            user_first_name = message.reply_to_message.sender_chat.first_name
        # TODO: L136

    elif len(message.command) > 1:
        if (
            len(message.entities) > 1 and
            message.entities[1].type == "text_mention"
        ):
            # 0: is the command used
            # 1: should be the user specified
            required_entity = message.entities[1]
            user_id = required_entity.user.id
            user_first_name = required_entity.user.first_name
        else:
            user_id = message.command[1]
            # don't want to make a request -_-
            user_first_name = user_id

        try:
            user_id = int(user_id)
        except ValueError:
            print("പൊട്ടൻ ")

    elif (
        message
    ):
        if message.from_user:
            user_id = message.from_user.id
            user_first_name = message.from_user.first_name

        # TODO: L136

        elif message.sender_chat:
            user_id = message.sender_chat.id
            user_first_name = message.sender_chat.title

    return (user_id, user_first_name)
