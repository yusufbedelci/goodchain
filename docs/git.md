## Guideline for version control in this project

### Branching

There will be two main branches for this project:

- **`dev`** → All active development occurs at the `dev` branch. Feature branches may be used locally and merged into `dev`.
- **`main`** → Reserved for working versions of the project. Changes are merged into `main` from `dev` once they are tested.

### Commit messages

All commit messages should be prefixed by the following labels to indicate their purpose:

- `feat: ` → Introduction of a new feature or functionality.
- `refactor: ` → Restructuring of existing code without changing behavior.
- `fix: ` → Fixing a bug or other unintended behaviors.
- `docs: ` → Documentation changes.
- `chore: ` → Maintenance tasks (setup, tooling, configuration, etc).
- `experimentation: ` → Educational changes, prototypes, or experimentational work that may not remain in the final codebase.
