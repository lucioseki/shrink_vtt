# Shrink VTT

A tool to trim Zoom-generated WebVTT file

# What's this?

Zoom web conference tool generates a transcript as a VTT file, which contains a sequence of captions. Each caption takes the following format:

```
SEQ
START_TIMESTAMP --> END_TIMESTAMP
PERSON: TEXT
```

Where:
- `SEQ`: a sequential number starting from 1
- `START_TIMESTAMP`: starting time in HH:mm:ss.SSS
- `END_TIMESTAMP`: starting time in HH:mm:ss.SSS
- `PERSON`: Name of the person speaking
- `TEXT`: The actual speech of the person

Example:
```
1
00:11:23.310 --> 00:11:24.340
Alice: Hello.

2
00:11:29.250 --> 00:11:30.390
Bob: Hi there.
```

Often, the speech is split into several captions:

```
188
00:24:16.870 --> 00:24:21.889
John Doe: Lorem ipsum dolor sit amet, consectetur adipiscing elit.

189
00:24:22.260 --> 00:24:26.219
John Doe: Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy.

190
00:24:26.960 --> 00:24:27.940
John Doe: Auctor massa. Pellentesque habitant morbi tristique senectus.
```

This is cumbersome when we want to read what someone spoke.

This tool addresses this issue by merging sequential captions of the same person into a single caption.

For instance, the sequence of captions above is merged into a single one:

```
188
00:24:16.870 --> 00:24:27.940
John Doe: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy.
Auctor massa. Pellentesque habitant morbi tristique senectus.
```

... which is way easier to read.

## Usage

1. Install the requirements

The recommended way is to use Virtualenv [0]:

```
virtualenv venv
source venv/bin/activate
(venv) pip install -r requirements.txt
```

2. Run the tool specifying the VTT file

```
python3 vttshrink.py <filename.vtt>
```

This will generate a new file `shrink.<filename.vtt>`.

## Known issues

- If two or more person are using the same name, their speech will be merged into one.
- If a person's name contains one or more colon (`:`) characters, it might lead into an unexpected behavior.

[0] Virtualenv: https://virtualenv.pypa.io/en/latest/installation.html
