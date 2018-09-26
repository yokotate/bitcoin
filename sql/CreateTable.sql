-- ビットコインの価格保存のためのSQL
-- DROP TABLE BTC_VALUE;
CREATE TABLE BTC_VALUE(
    id SERIAL,
    last_val int,
    bid_val int,
    ask_val int,
    high_val int,
    low_val int,
    volume_val int
);

-- ユーザ情報
-- DROP TABLE USERDATA;
CREATE TABLE USERDATA(
	Money bigint,				-- 所持金額
	BitCoin bigint,				-- 所持ビットコイン量
	BitCoinBuyValue bigint,		-- 取得時ビットコイン価格
	BitCoinFlag Boolean			-- ビットコイン所持フラグ
);
