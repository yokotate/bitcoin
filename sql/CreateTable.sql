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
	Money numeric(15,8),				-- 所持金額
	BitCoin numeric(15,8),				-- 所持ビットコイン量
	BitCoinBuyMoney numeric(15,8),		-- 取得時現金
	BitCoinBuyValue numeric(15,8),		-- 取得時ビットコイン価格
	BitCoinFlag Boolean			-- ビットコイン所持フラグ
);
-- テストデータ
-- insert into userdata values (10000,0,0,0,FALSE);


