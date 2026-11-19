// Entry for make.fun bounty gta6-meme-x-01 (Node 22, standard library only).
//
// The entry is the X post itself: the meme picture and its text are what the
// judge reads. This program only hands the post's address to the grader --
// it copies POST.json from the repository root into the output directory.
// It uses no network, no clock, and no files outside the repository, so two
// runs write the same bytes.
//
// Run it locally the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outputDir, { recursive: true });

try {
  copyFileSync(join(botDir, "POST.json"), join(outputDir, "POST.json"));
} catch (error) {
  console.error(
    `Could not copy POST.json out of ${botDir}: ${(error as Error).message}`,
  );
  process.exit(1);
}
