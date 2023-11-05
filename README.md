# ai_subtitle_editor

Simple application to translate srt subtitle files using OpenAI's API

## Installation

### Prerequisites

- Python 3
- An OpenAI API key is required (get one [here](https://platform.openai.com/account/api-keys))

### Installation

1. Clone the repo `git clone https://github.com/patrickgil/ai_subtitle_editor`
2. Rename the example `.env.example` to `.env` and paste your OpenAI API key

### Usage

```bash
python main.py <srt filename>
```

#### Note

All .srt files need to follow standard naming convention:

```bash
filename.ISO_language_code.srt
```