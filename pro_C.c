#include <stdio.h>
#include <string.h>

#define MAX_MEANINGS 10

typedef struct {
    char part_of_speech[20];
    char meanings[MAX_MEANINGS][100];
    int num_meanings;
} WordDefinition;

WordDefinition get_meanings(char* word) {
    // 単語の意味を取得する処理を実装する
    WordDefinition definition;
    
    // 仮の意味を設定
    strcpy(definition.part_of_speech, "noun");
    strcpy(definition.meanings[0], "meaning 1");
    strcpy(definition.meanings[1], "meaning 2");
    definition.num_meanings = 2;
    
    return definition;
}

void display_meanings(WordDefinition definition) {
    printf("%s:\n", definition.part_of_speech);
    for (int i = 0; i < definition.num_meanings; i++) {
        printf("- %s\n", definition.meanings[i]);
    }
}

int main() {
    char word[100];
    WordDefinition definition;
    
    printf("単語を入力してください: ");
    scanf("%s", word);
    
    definition = get_meanings(word);
    
    if (definition.num_meanings > 0) {
        display_meanings(definition);
    } else {
        printf("意味が見つかりませんでした。\n");
    }
    
    return 0;
}

