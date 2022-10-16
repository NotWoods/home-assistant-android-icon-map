declare module "@mdi/util" {
  export interface IconMeta {
    id: string;
    name: string;
    codepoint: string;
    aliases: string[];
    tags: string[];
    author: string;
    version: string;
  }

  export function getVersion(): string;

  export function getMeta(withPaths?: boolean): IconMeta[];
}
