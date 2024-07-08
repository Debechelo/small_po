# 4.* Написать скрипт очистки директорий. На вход принимает путь к директории.
#    Если директория существует, то удаляет в ней все файлы с расширениями .bak, .tmp, .backup.
#    Если директории нет, то выводит ошибку.

cleanup_directory() {
    local dir="$1"
    if [ -d "$dir" ]; then
        find "$dir" -type f \( -name "*.bak" -o -name "*.tmp" -o -name "*.backup" \) -delete
        echo "Файлы .bak, .tmp, .backup успешно удалены из директории $dir."
    else
        echo "Директория $dir не существует."
    fi
}

cleanup_directory "/home/user/directory"