import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))