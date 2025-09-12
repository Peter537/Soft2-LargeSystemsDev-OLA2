
## 1. Getting Started
- Clone the repo: `git clone https://github.com/Peter537/Soft2-LargeSystemsDev-OLA2`

- Verificere at dit environment er sat op, ved at køre projektet og tests via `dotnet run` og `dotnet test`.

## 2. Branching Rules
- Brug GitHub Flow branching strategi. 
- Altid opret en ny branch fra `main` for hver ny feature eller bugfix.

## 3. Commit Message Guidelines
- Brug klare og beskrivende commit beskeder.

- Commit beskeder skal være i imperativ form og på engelsk, fx "Add user authentication feature" eller "Fix null reference exception in UserService".

- Krav: Tilføj altid et Issue-reference i footer.

    - Auto-luk: `Closes #123` / `Fixes #123`

    - Kun reference: `#123` eller `Refs #123`

- Typer: `feat`, `fix`, `docs`, `style`, `refactor`, `test`

- Scope: valgfri (`auth`, `ui`, `api`)

- Format: 
    1. `<type>(<scope>): <subject>` (fx `feat(auth): add user login functionality`)
    2. `<type>(<scope>): <subject> <footer>` (fx `fix(api): resolve null pointer exception Closes #45`)
        - 2.1 hvis man bruger github desktop, så kan man have: 

            **Summary**: feat(auth): add user login functionality

            **Description**: Closes #123
        

## 4. Code Style Rules
- Følg C# coding conventions som beskrevet i [Microsoft's C# Coding Conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions).


## 5. Expected Workflow
- Åben Issue -> Opret Branch -> Lav Commits -> Push til main -> Automatisk CI pipeline kører -> Issue lukkes