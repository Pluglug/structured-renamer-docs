function switchLanguage(lang) {
    // 現在のページのパスを取得
    const currentPath = window.location.pathname;
    // 現在の言語ディレクトリを取得（存在する場合）
    const currentLang = currentPath.split('/')[1];
    // 新しいパスを構築
    let newPath;
    if (currentLang === 'ja' || currentLang === 'en') {
        // すでに言語ディレクトリがある場合は置換
        newPath = currentPath.replace(`/${currentLang}/`, `/${lang}/`);
    } else {
        // 言語ディレクトリがない場合は追加
        const pathParts = currentPath.split('/');
        pathParts.splice(1, 0, lang);
        newPath = pathParts.join('/');
    }
    // 新しいURLに移動
    window.location.href = newPath;
} 