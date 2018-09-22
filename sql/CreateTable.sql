-- ビットコインの価格保存のためのSQL
DROP TABLE BTC_VALUE;
CREATE TABLE BTC_VALUE(
    id SERIAL,
    last_val int,
    bid_val int,
    ask_val int,
    high_val int,
    low_val int,
    volume_val int
);

