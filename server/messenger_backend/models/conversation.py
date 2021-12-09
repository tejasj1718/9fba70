from django.db import models
from django.db.models import Q

from . import utils
from .user import User


class Conversation(utils.CustomModel):

    user1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user1Id",
        related_name="+"
    )
    user2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user2Id",
        related_name="+",
    )

    last_read_message_user1 = models.ForeignKey('Message',
                                                on_delete=models.SET_NULL,
                                                null=True,
                                                default=None,
                                                related_name='+')

    last_read_message_user2 = models.ForeignKey('Message',
                                                on_delete=models.SET_NULL,
                                                null=True,
                                                default=None,
                                                related_name='+')

    createdAt = models.DateTimeField(auto_now_add=True, db_index=True)
    updatedAt = models.DateTimeField(auto_now=True)

    # find conversation given two user Ids
    @staticmethod
    def find_conversation(user1Id, user2Id):
        # return conversation or None if it doesn't exist
        try:
            return Conversation.objects.get(
                (Q(user1__id=user1Id) | Q(user1__id=user2Id)),
                (Q(user2__id=user1Id) | Q(user2__id=user2Id)),
            )
        except Conversation.DoesNotExist:
            return None

    @staticmethod
    def get_unread_message_count(messages, last_read_message, other_user_id):
        print(messages)
        print(None if last_read_message is None else last_read_message.id)
        print(other_user_id)
        message_count = 0
        reachedLastMessage = last_read_message is None
        for message in messages:
            if message['senderId'] == other_user_id:
                if reachedLastMessage:
                    message_count += 1
                elif message['id'] == last_read_message.id:
                    reachedLastMessage = True

        return message_count
