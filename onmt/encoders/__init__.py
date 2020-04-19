"""Module defining encoders."""
from onmt.encoders.encoder import EncoderBase
from onmt.encoders.transformer import TransformerEncoder


str2enc = {"transformer": TransformerEncoder}

__all__ = ["EncoderBase", "TransformerEncoder", "str2enc"]
