
# Knowledge Center Automation

Script automation for auto update from repo to knowledge center


## Authors

- [AdamSH](adam@majoo.id)


## Documentation

- Clone this script inside target root repository 
- Has `Readme.MD` file inside root repository 
- Has `docs` folder in root repository 
- If folder has `Readme.MD` file inside each folder in `docs` directory, automatically become description in document
- `Markdown` type only will be readed
- If folder doesn't have any children will not be readed
- Any file name will convert with capitalize each word and remove extension. ex: `tech_stack.md` to `Tech Stack` document

## Run Locally


Prerequisite
- Install Python

Clone this repository

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Start script

```bash
  python main.py --name <name for this project> --token <api-token>
```

Check outline

```
  go to outline server 
```

## Tech Stack

**Tool:** Outline

**Server:** Python


## Support

For support, email adamsyarif219@gmail.com.

