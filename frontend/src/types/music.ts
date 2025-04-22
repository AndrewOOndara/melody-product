export interface Track {
    id: string;
    name: string;
    artist: string;
    album: string;
    spotify_url: string;
    preview_url: string | null;
    album_art: string | null;
    release_date: string;
    label: string;
    discogs_info?: DiscogsInfo;
}

export interface DiscogsInfo {
    title: string;
    artist: string;
    year: string;
    label: string;
    format: string;
    discogs_url: string;
    thumbnail: string | null;
}

export interface SearchResponse {
    results: Track[];
}

export interface SubscribeResponse {
    message: string;
} 