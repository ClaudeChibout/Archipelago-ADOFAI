# ADOFAI – Setup Guide

## 📦 Prerequisites

- **Archipelago**: Minimum recommended version: `6.3.0`
- **ADOFAI**: Stable version compatible with the world
- **Client**: [BepInEx Mod Client](https://github.com/ClaudeChibout/ADOFAI_AP-Mod/releases/tag/v2.0.0-beta)
- Stable internet connection

---

## 📥 Mod Installation

1. Drag the contents of the client archive into the ADOFAI installation folder

---

## ⚙️ Slot Configuration

Configuration is done from the **player options page**:  
👉 [ADOFAI Player Options](../player-options)

### Available Options

| Option | Description |
|--------|-------------|
| **percentage_goal_completion** | Percentage of levels to complete for victory |
| **completion_goal** | Final goal mode (`allX`, `goalLevels`) |
| **goal_levels** | List of required levels if `completion_goal = goalLevels` |
| **main_worlds_tuto** | Includes tutorials from main worlds |
| **xtra_worlds** | Adds xtra worlds |
| **xtra_worlds_tuto** | Adds tutorials from xtra worlds |
| **b_world** | Adds world B |
| **b_world_tuto** | Adds tutorial for world B |
| **crown_worlds** | Adds “Crown” worlds |
| **crown_worlds_tuto** | Adds tutorials for “Crown” worlds |
| **star_worlds** | Adds “Star” worlds |
| **star_worlds_tuto** | Adds tutorials for “Star” worlds |
| **neon_cosmos_worlds** | Adds standard “Neon Cosmos” worlds |
| **neon_cosmos_worlds_tuto** | Adds standard “Neon Cosmos” tutorials |
| **neon_cosmos_worlds_ex** | Adds “Neon Cosmos EX” worlds |
| **neon_cosmos_worlds_ex_tuto** | Adds “Neon Cosmos EX” tutorials |
| **april_fools_worlds** | Adds “April Fools” worlds |
| **cosmic_radio_worlds** | Adds “Cosmic Radio” worlds (CE, CI) |
| **cosmic_radio_worlds_tuto** | Adds tutorials for “Cosmic Radio” worlds |
| **cosmic_radio_worlds_ex** | Adds the “Cosmic Radio EX” world (CE-TX, very hard) |
| **death_link** | Enables DeathLink between players |

---

## 🎮 Start a Local Game

1. Place your YAML file in `Archipelago\Players`
2. In **Archipelago**, select **Generate**
3. In **Archipelago**, select **Host** and choose the newly created archive in `Archipelago\output`

---

## 🌍 Play in Multiworld

1. Host an Archipelago server or join another player’s server
2. Retrieve the `.yaml` configuration file for your slot
3. Launch the game with the configured client (modified ADOFAI)
4. Connect to the server using:
- **Address**
- **Port**
- **Slot name**

---

## 🏁 Goal and Progression

- **Start**: You begin with access to a small number of initial levels
- **Progression**: Each completed level grants an **item**
- **Victory**: Fulfill your victory conditions specified in your YAML to win
