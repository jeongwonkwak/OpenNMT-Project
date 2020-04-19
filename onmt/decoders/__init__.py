"""Module defining decoders."""
from onmt.decoders.decoder import DecoderBase
from onmt.decoders.transformer import TransformerDecoder


str2dec = {"transformer": TransformerDecoder}

__all__ = ["DecoderBase", "TransformerDecoder", "str2dec"]
