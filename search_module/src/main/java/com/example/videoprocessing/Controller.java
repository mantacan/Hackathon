package com.example.videoprocessing;


import lombok.RequiredArgsConstructor;
import org.elasticsearch.index.query.QueryBuilders;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.data.elasticsearch.client.elc.NativeQueryBuilder;
import org.springframework.data.elasticsearch.core.ElasticsearchOperations;
import org.springframework.data.elasticsearch.core.SearchHit;
import org.springframework.data.elasticsearch.core.SearchHits;
import org.springframework.data.elasticsearch.core.query.Query;
import org.springframework.data.elasticsearch.core.query.SearchTemplateQuery;
import org.springframework.data.elasticsearch.core.query.StringQuery;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.reactive.function.client.WebClient;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;


@RestController
@RequiredArgsConstructor
public class Controller {
    @Autowired
    private VideoService videoService;
    @Autowired
    private WebClient webClient;

    private final ElasticsearchOperations elasticsearchOperations;


    @PostMapping(value = "/index",
            consumes = MediaType.APPLICATION_JSON_VALUE,
            produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseStatus(HttpStatus.CREATED)
    public ResponseEntity<Map<String, Object>> redirect(@RequestBody Map<String, Object> request) {
        Map<String, Object> response = webClient.post()
                .uri("http://147.45.237.137:5000/processing")
                .bodyValue(request)
                .retrieve()
                .bodyToMono(new ParameterizedTypeReference<Map<String, Object>>() {})
                .block();

        videoService.indexData(response);

        return ResponseEntity.ok(response);
    }


    @GetMapping(value = "/search")
    public List<String> search(@RequestParam String text) {
        Query searchQuery = new StringQuery(text);

        SearchHits<String> searchHits = elasticsearchOperations.search(searchQuery, String.class);

        return searchHits.stream().map(SearchHit::getContent).collect(Collectors.toList());
    }

}
