# Object-Oriented Programming (OOP) — Concepts & Examples

This README summarizes core Object-Oriented Programming (OOP) concepts with short Python examples, best practices, and a quick guide to push this file to Git.

## High-level contract
- Inputs: code and concepts in this repo's Python files.
- Outputs: README.md explaining OOP principles and an attempted git push.
- Success: README created and committed; push succeeds or clear next steps provided.

## Core OOP Concepts
1. Encapsulation
   - Group related data (attributes) and functions (methods) inside classes.
   - Use access controls (convention: `_private`, `__name` in Python) to hide internal state.

   Example:
   ```python
   class BankAccount:
       def __init__(self, owner, balance=0):
           self.owner = owner
           self._balance = balance  # _ indicates internal use

       def deposit(self, amount):
           if amount > 0:
               self._balance += amount

       def withdraw(self, amount):
           if 0 < amount <= self._balance:
               self._balance -= amount
               return amount
           raise ValueError('Insufficient funds')

       def get_balance(self):
           return self._balance
   ```

2. Abstraction
   - Expose a simple public interface and hide complexity.
   - Keep high-level operations readable and limited.

3. Inheritance
   - Reuse and extend behavior from a parent class.
   - Avoid deep hierarchies; prefer composition when it simplifies design.

   Example:
   ```python
   class Animal:
       def speak(self):
           raise NotImplementedError

   class Dog(Animal):
       def speak(self):
           return 'Woof'
   ```

4. Polymorphism
   - Different types implement the same interface; code uses them interchangeably.

   Example:
   ```python
   animals = [Dog(), /* another Animal subclass */]
   sounds = [a.speak() for a in animals]
   ```

## Design guidelines & best practices
- Single Responsibility Principle (SRP): each class should have one reason to change.
- Prefer composition over inheritance for greater flexibility.
- Keep methods small and focused.
- Write unit tests for public behaviors, not implementation details.

## Quick Git push guide (PowerShell on Windows)
If this workspace is already a Git repo and has a configured remote, these steps will add, commit and push the README.

1. Stage and commit the README:

```powershell
cd "c:\vscode tool\chapter 10 oops"
git add README.md
git commit -m "Add README: OOP concepts"
```

2. Push to the remote (example for `origin` and branch `main`):

```powershell
git push origin main
```

If you haven't created a remote repo on GitHub/GitLab/Bitbucket yet:
- Create a new repository on the hosting service.
- Follow the site's "push an existing repository from the command line" instructions, for example:

```powershell
git remote add origin https://github.com/your-username/your-repo.git
git branch -M main
git push -u origin main
```

Authentication note: modern Git hosts usually require a PAT (Personal Access Token) or SSH key rather than a password. If `git push` fails, check the error message and follow the provider's auth guidance.

## Examples & Next steps
- Add short unit tests to demonstrate OOP patterns (e.g., test BankAccount deposit/withdrawal).
- Add class diagrams or UML if helpful.

---
If you want, I can now attempt to run the git commands to add/commit/push the README and show the output. If you prefer I can only provide instructions instead. Which would you like me to do?