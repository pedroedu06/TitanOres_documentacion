# Development Setup

## Requirements

| Tool | Version |
|---|---|
| JDK to **run Gradle** | 17 or newer (the project is developed with JDK 21) |
| JDK to **compile and run the mod** | 8 (Gradle toolchain) |
| Gradle | 8.8 (wrapper, no install needed) |
| ForgeGradle | 6.0.x |
| Mappings | official (Mojang) 1.16.5 |

If Gradle does not find your JDK 8 automatically, point to it in your **user** Gradle properties
(`~/.gradle/gradle.properties`, never in the project):

```properties
org.gradle.java.installations.paths=C:/path/to/jdk-8
```

## Common tasks

| Command | What it does |
|---|---|
| `gradlew build` | Builds the mod jar into `build/libs/titanores-<version>.jar` |
| `gradlew runClient` | Starts Minecraft with the mod (development environment) |
| `gradlew runServer` | Starts a dedicated server |
| `gradlew genIntellijRuns` / `genEclipseRuns` | Creates IDE run configurations |
| `gradlew processResources` | Copies the resources again (use with F3+T or `/reload` while the game is open) |

!!! warning "Testing with other mods"
    Jars downloaded from CurseForge are obfuscated and **crash** the development environment if dropped into
    `run/mods`. Add them through `build.gradle` instead, for example
    `runtimeOnly fg.deobf("group:artifact:version")`. This is how Curios is added.

## Live reload cheatsheet

| Changed | How to see it |
|---|---|
| Textures, models, lang | `gradlew processResources`, then **F3+T** |
| Recipes, loot tables, tags | `gradlew processResources`, then `/reload` |
| Java code | restart `runClient` |
