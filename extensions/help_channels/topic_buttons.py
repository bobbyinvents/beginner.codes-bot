from dataclasses import dataclass
from nextcord import ButtonStyle, PartialEmoji
from nextcord.components import SelectOption
from nextcord.ui import Button, Select, View
from typing import Optional, Union
import re


@dataclass
class Option:
    label: str
    emoji: Union[str, PartialEmoji]
    type: str = "option"
    custom_value: Optional[str] = None

    @property
    def value(self) -> str:
        return self.custom_value or re.sub(r"[^a-z0-9]+", "_", self.label.casefold())


class Language(Option):
    type = "language"


class Topic(Option):
    type = "topic"


languages = [
    Language("C", PartialEmoji(name="clang", id=934951942029979688)),
    Language(
        "C#", PartialEmoji(name="c_sharp", id=947603932161667132), custom_value="cs"
    ),
    Language(
        "C++", PartialEmoji(name="cpp", id=947603931519926342), custom_value="cpp"
    ),
    Language("Java", PartialEmoji(name="java", id=934957425587523624)),
    Language("JavaScript", PartialEmoji(name="javascript", id=908457207597764678)),
    Language("PHP", "🐘"),
    Language("Python", PartialEmoji(name="python", id=934950343614275594)),
    Language("TypeScript", PartialEmoji(name="typescript", id=982974090400923689)),
]

topics = [
    Topic("Discord Bot", "🤖"),
    Topic("Django", PartialEmoji(name="django", id=947586026786938880)),
    Topic("Docker and Kubernetes", "📦", custom_value="docker"),
    Topic("Ethical Hacking", "🚨", custom_value="hacking"),
    Topic("FastAPI", "🏎", custom_value="fast-api"),
    Topic("Flask", "🍶"),
    Topic("Game Development", "🕹"),
    Topic("Homework", "📓"),
    Topic("Machine Learning", "🧠"),
    Topic("React", PartialEmoji(name="react", id=947584730319179826)),
    Topic("Windows", "🪟", custom_value="windows-os"),
    Topic("Linux/MacOS", "🖥", custom_value="unix-os"),
    Topic("Code Editor/IDE", "📝", custom_value="editor"),
    Topic(
        "Web Development",
        PartialEmoji(name="webdev", id=934956458938880050),
        custom_value="webdev",
    ),
]


def create_view() -> View:
    view = View(timeout=None)
    view.add_item(
        Select(
            custom_id="bc.help.language",
            placeholder="Select a language",
            row=1,
            options=[
                SelectOption(label=lang.label, value=lang.value, emoji=lang.emoji)
                for lang in languages
            ],
        )
    )
    view.add_item(
        Select(
            custom_id="bc.help.topic",
            placeholder="Select a help category (optional)",
            max_values=2,
            row=2,
            options=[
                SelectOption(label=topic.label, value=topic.value, emoji=topic.emoji)
                for topic in topics
            ],
        )
    )
    view.add_item(
        Button(
            custom_id="bc.help.claim_button",
            label="Claim Channel",
            style=ButtonStyle.blurple,
            row=3,
        )
    )
    return view
